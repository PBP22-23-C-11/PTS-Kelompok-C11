from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.core import serializers

from general.utils import check_user_type, customer_required, get_user_type, type_required, umkm_required, get_user_name
from general.constants import UserType

from .constants import *
from .utils import *
from .models import *
from .forms import *

# Pages
def news_page_umkm(request):
    context = {
        'is_customer': check_user_type(request.user) == UserType.Customer,
        'is_umkm': check_user_type(request.user) == UserType.UMKM,
        'is_admin': check_user_type(request.user) == UserType.Admin,
        'category': 'umkm',
        'umkm_button_class': 'category-pressed',
    }
    return render(request, 'news.html', context)

def news_page_official(request):
    context = {
        'is_customer': check_user_type(request.user) == UserType.Customer,
        'is_umkm': check_user_type(request.user) == UserType.UMKM,
        'is_admin': check_user_type(request.user) == UserType.Admin,
        'category': 'official',
        'official_button_class': 'category-pressed',
    }
    return render(request, 'news.html', context)

@login_required(login_url='/login/')
@customer_required
def news_page_subscribed(request):
    return render(request, 'news.html')

@login_required(login_url='/login/')
@type_required(types=[UserType.Admin, UserType.UMKM])
def create_page(request):
    return render(request, 'create_article.html')

def article_page(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return HttpResponse(status=404)
    context = {
        'article': article,
        'author_name': get_user_name(article.author_user),
        'is_author': request.user == article.author_user,
        'is_logged_in': request.user.is_authenticated,
        'user_id': request.user.id,
        'comment_form': CommentForm(),
    }
    return render(request, 'article.html', context)

# API
# Articles
def article(request):
    if request.method == 'GET':
        return get_article(request)
    elif request.method == 'POST':
        return post_article(request)
    
    return HttpResponse(status=404)

def get_article(request):
    # Params
    title = request.GET.get('title', '')
    sort_by = request.GET.get('sort_by')
    if sort_by not in SortBy.VALUES:
        sort_by = SortBy.VALUES[0]
    category = request.GET.get('category')
    if category not in Category.VALUES:
        category = Category.VALUES[0]
    
    if category == Category.UMKM:
        # Params
        umkm = request.GET.get('umkm', '')
        umkm_type = request.GET.get('umkm_type')
        if umkm_type not in UMKMType.VALUES:
            umkm_type = UMKMType.VALUES[0]
            
        if umkm_type == UMKMType.USERNAME:
            article_list = UMKMArticle.objects.filter(article__title__startswith=title, article__author_user__username__startswith=umkm)
            
        elif umkm_type == UMKMType.NAME:
            article_list = UMKMArticle.objects.filter(article__title__startswith=title, author_umkm__name__startswith=umkm)
        
        else:
            article_list = UMKMArticle.objects.filter(article__title__startswith=title)
        
    elif category == Category.OFFICIAL:
        article_list = OfficialArticle.objects.filter(article__title__startswith=title)
        
    elif category == Category.SUBSCRIBED and request.customer_data is not None:
        subscribe_list = get_subscribed_id(request.user)
        article_list = UMKMArticle.objects.filter(article__title__startswith=title, article__author_user__id__in=subscribe_list)
        
    else:
        return HttpResponse(status=404)
    
    article_list = article_list.annotate(likes=Count('article__like'))
    article_list = article_list.order_by(SortBy.convert(sort_by))
    
    article_list_json = []
    for article in article_list:
        article_json = {
            'id': article.article.id,
            'author': {
                'id': article.article.author_user.id,
                'name': get_user_name(article.article.author_user),
            },
            'title': article.article.title,
            'body': article.article.body,
            'created_at': article.article.created_at,
            'updated_at': article.article.updated_at,
        }
        article_list_json.append(article_json)
    
    return JsonResponse({
        'articles': article_list_json,
    })

@login_required
@type_required(types=[UserType.Admin, UserType.UMKM])
@get_user_type
def post_article(request):
    user_type = check_user_type(request.user)
    
    title = request.POST.get('title')
    body = request.POST.get('body')
    created_at = timezone.now()
    updated_at = created_at
    
    article = Article.objects.create(
        author_user=request.user,
        title=title,
        body=body,
        created_at=created_at,
        updated_at=updated_at
    )
    article_json = {
        'id': article.id,
        'author': {
            'id': article.author_user.id,
            'name': get_user_name(article.author_user),
        },
        'title': article.title,
        'body': article.body,
        'created_at': article.created_at,
        'updated_at': article.updated_at,
    }
    
    if user_type == UserType.Admin:
        OfficialArticle.objects.create(article=article)
    else:
        UMKMArticle.objects.create(author_umkm=request.umkm_data, article=article)
    
    return JsonResponse(article_json)

@login_required
def article_by_id(request, article_id): # PUT, and DELETE
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return HttpResponse(status=404)
    if request.user.id == article.author_user.id:
        if request.method == 'DELETE':
            return delete_article_by_id(request, article)
    return HttpResponse(status=404)

def delete_article_by_id(request, article : Article):
    article.delete()
    return HttpResponse(status=204)

# Comments (Accessible by logged in users only)
@login_required
def article_comments(request, article_id): # GET and POST
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        return get_article_comments(request, article)
    elif request.method == 'POST':
        return post_article_comment(request, article)
    return HttpResponse(status=404)

def get_article_comments(request, article):
    comment_list = Comment.objects.filter(article=article)
    comment_list_json = []
    for comment in comment_list:
        comment_json = {
            'user': {
                'id': comment.user.id,
                'name': get_user_name(comment.user),
            },
            'id': comment.id,
            'body': comment.body,
        }
        comment_list_json.append(comment_json)
    return JsonResponse({
        'comments': comment_list_json,
    })

def post_article_comment(request, article):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return HttpResponse(status=201)
    return HttpResponse(status=400)

@login_required
def article_comment_by_id(request, article_id, comment_id): # DELETE
    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return HttpResponse(status=404)
    if request.user.id == comment.user.id and comment.article.id == article_id:
        if request.method == 'DELETE':
            return delete_comment(request, comment)
    return HttpResponse(status=404)

def delete_comment(request, comment : Comment):
    comment.delete()
    return HttpResponse(status=204)

# Like
@login_required
@customer_required
def update_article_like(request, article_id):
    pass

# Subscribe
@login_required
@customer_required
def update_subscribe(request, user_id):
    pass
from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path('', news_page_umkm, name='news_page_umkm'),
    path('official/', news_page_official, name='news_page_official'),
    path('subscribed/', news_page_subscribed, name='news_page_subscribed'),
    path('api/article/', article, name='article'),
    path('<int:article_id>/', article_page, name='article_page'),
    path('api/articles/<int:article_id>/', article_by_id, name='article_by_id'),
    path('api/articles/<int:article_id>/comments/', article_comments, name='article_comments'),
    path('api/articles/<int:article_id>/comments/<int:comment_id>/', article_comment_by_id, name='article_comment_by_id'),
    path('api/articles/<int:article_id>/likes/', like, name='like'),
    path('api/subscribes/<int:author_id>/', subscribe, name='subscribe'),
]
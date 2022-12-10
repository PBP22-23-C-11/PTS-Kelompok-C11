from audioop import reverse
import json
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from general.utils import check_user_type
from obrolan.forms import DiscussionForm
from obrolan.models import Diskusi
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.
def show_obrolan(request):
    type = check_user_type(request.user) # 0=UMKM, 1=Cust
    if (type==0):
        tipe_user = "UMKM"
        opposite = "Customer"
    elif (type==1):
        tipe_user = "Customer"
        opposite = "UMKM"
    else:
        tipe_user = "Admin"
        opposite = "UMKM, Customer"

    users = User.objects.all()
    opposite_user = []
    for user in users:
        if (type != check_user_type(user)) and (check_user_type(user) != 2):
            opposite_user.append(user.username)

    user_and_type = dict()
    for user in users:
        type = check_user_type(user)
        if (type==0):
            user_and_type[user.username] = "UMKM"
        elif (type==1):
            user_and_type[user.username] = "Customer"
        else:
            user_and_type[user.username] = "Admin"

    context = {
        'form': DiscussionForm(),
        'users': opposite_user,
        'tipe_user': tipe_user,
        'opposite': opposite,
        'user_and_type': user_and_type,
    }
    if request.user.is_authenticated:
        return render(request, "obrolan.html", context)
    else:
        return render(request, "obrolan_not_logged_in.html", context)

def show_diskusi_json(request):
    data = Diskusi.objects.all().order_by('id')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
@csrf_exempt
def create_diskusi_ajax(request):

    if request.method == "POST":
        user=request.user
        username=user.username
        title = request.POST['title']
        if (title.strip()==""):
            title = "Reply"
        toWho = request.POST['toWho']
        message = request.POST['message']
        date = datetime.datetime.now(datetime.timezone.utc)+ datetime.timedelta(hours=7)
        Diskusi.objects.create(user=user, username=username, date=date, title=title, toWho=toWho, message=message)
        return JsonResponse({'error': False, 'msg':'Successful'})
    
    return redirect('obrolan:show_obrolan')

@login_required(login_url='/login/')
@csrf_exempt
def delete_disc(request, id):
    if request.method == "POST":
        disc = get_object_or_404(Diskusi, pk=id, user=request.user)
        disc.delete()
        return JsonResponse({'error':False})

@csrf_exempt
def create_diskusi_flutter(request):
    if request.method == 'POST':
        user = request.user
        data = json.loads(request.body)
        username = data["username"]
        date = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=7)
        title = data["title"]
        toWho = data["toWho"]
        message = data["message"]
        Diskusi.objects.create(user=user, username=username, date=date, title=title, toWho=toWho, message=message)
        return JsonResponse({"status": "success"}, status = 200)
    else:
        return JsonResponse({"status": "error"}, status = 401)

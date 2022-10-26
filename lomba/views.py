from django.shortcuts import render
from django.http import HttpResponse
from general.utils import *

# Create your views here.
def show_lomba(request):
    check = check_user_type(request.user)
    context = {
        'user': request.user,
        'check': check,
    }
    return render(request, "lomba.html", context)

def buat_lomba(request):
    return HttpResponse('Welcome Admin')

def daftar_lomba(request):
    return HttpResponse('Welcome UMKM')

def vote_lomba(request):
    return HttpResponse('Welcome Customer')
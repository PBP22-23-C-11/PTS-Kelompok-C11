from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from general.constants import UserType

from .models import UMKM, Customer
from .utils import admin_required, get_user_type, none_required, type_required, umkm_required, customer_required

# General Pages
def landing_page(request):
    return HttpResponse('Welcome to landing page!')
    
# Examples
@login_required(login_url='/login') # mengharuskan user untuk login
@umkm_required # mengecek apakah user merupakan akun UMKM
@get_user_type # membuat atribut request.umkm_data yang mengarah pada model UMKM
def example_umkm_only_page(request):
    return HttpResponse(f'Username: {request.user.username}, Nama UMKM: {request.umkm_data.name}')

@login_required(login_url='/login') # mengharuskan user untuk login
@customer_required # mengecek apakah user merupakan akun customer
@get_user_type # membuat atribut request.customer_data yang mengarah pada model Customer
def example_customer_only_page(request):
    return HttpResponse(f'Username: {request.user.username}, Name: {request.customer_data.first_name} {request.customer_data.last_name}')

# User Functions
# TODO: change to AJAX-based login (?)
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('landing_page'))
        else:
            messages.error('User not found')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_user'))

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        login(request, user)
        return JsonResponse({
            'message': 'Akun berhasil dibuat',
        })
    return render(request, 'register_user.html')

@login_required(login_url='/login')
@none_required
def register_type(request):
    context = {
        'username': request.user.username,
    }
    return render(request, 'register_type.html', context)

@login_required(login_url='/login')
@none_required
def register_umkm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        UMKM.objects.create(user=request.user, name=name)
        return JsonResponse({
            'message': 'Data UMKM berhasil dimasukkan',
        })
    return HttpResponse(status=404)

@login_required(login_url='/login')
@none_required
def register_customer(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        Customer.objects.create(user=request.user, first_name=first_name, last_name=last_name)
        return JsonResponse({
            'message': 'Data Customer berhasil dimasukkan',
        })
    return HttpResponse(status=404)

@login_required
def get_logged_in_user_id(request):
    return JsonResponse({'id':request.user.id})
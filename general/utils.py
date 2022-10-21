from atexit import register
from urllib import request
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Customer, UMKM
from .constants import UserType

# Fungsi hanya dapat diakses oleh pengguna yang belum menyelesaikan registrasi tahap 2 (pemilihan role)
def none_required(function, register_url = None):
    def inner(request, *args, **kwargs):
        if check_user_type(request.user) == None:
            return function(request, *args, **kwargs)
        
        if register_url == None:
            return HttpResponse(status=404)
        else:
            return redirect(register_url)
    
    return inner

# Fungsi hanya dapat diakses oleh pengguna UMKM
def umkm_required(function, register_url = None):
    def inner(request, *args, **kwargs):
        if check_user_type(request.user) == UserType.UMKM:
            return function(request, *args, **kwargs)
        
        if register_url == None:
            return HttpResponse(status=404)
        else:
            return redirect(register_url)
    
    return inner

# Fungsi hanya dapat diakses oleh pengguna Customer
def customer_required(function, register_url = None):
    def inner(request, *args, **kwargs):
        if check_user_type(request.user) == UserType.Customer:
            return function(request, *args, **kwargs)
        
        if register_url == None:
            return HttpResponse(status=404)
        else:
            return redirect(register_url)
    
    return inner

# Mendapatkan request.umkm_data atau request.customer_data (perlu dipastikan bahwa user sudah terlogin melalui @login_required)
def get_user_type(function):
    def inner(request, *args, **kwargs):
        try:
            umkm = UMKM.objects.get(user__id=request.user.id)
            request.umkm_data = umkm
        except:
            pass
        
        try:
            customer = Customer.objects.get(user__id=request.user.id)
            request.customer_data = customer
        except:
            pass
        
        return function(request, *args, **kwargs)
    
    return inner

# Mengecek jenis user
def check_user_type(user):
    umkm_count = UMKM.objects.filter(user__id=user.id).count()
    customer_count = Customer.objects.filter(user__id=user.id).count()
    
    if umkm_count == 1:
        return UserType.UMKM
    elif customer_count == 1:
        return UserType.Customer
    else:
        return None
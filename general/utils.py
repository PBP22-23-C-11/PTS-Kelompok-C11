from atexit import register
from urllib import request
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Customer, UMKM
from .constants import UserType

# Fungsi hanya dapat diakses oleh pengguna yang belum menyelesaikan registrasi tahap 2 (pemilihan role)
def none_required(function):
    def inner(request, *args, **kwargs):
        if check_user_type(request.user) == None:
            return function(request, *args, **kwargs)
        return HttpResponse(status=404)
    return inner

# Fungsi hanya dapat diakses oleh pengguna UMKM
def umkm_required(function):
    def inner(request, *args, **kwargs):
        if check_user_type(request.user) == UserType.UMKM:
            return function(request, *args, **kwargs)
        return HttpResponse(status=404)
    return inner

# Fungsi hanya dapat diakses oleh pengguna Customer
def customer_required(function):
    def inner(request, *args, **kwargs):
        if check_user_type(request.user) == UserType.Customer:
            return function(request, *args, **kwargs)
        return HttpResponse(status=404)
    return inner

# Fungsi hanya dapat diakses oleh admin
def admin_required(function):
    def inner(request, *args, **kwargs):
        if check_user_type(request.user) == UserType.Admin:
            return function(request, *args, **kwargs)
        return HttpResponse(status=404)
    return inner

# Fungsi hanya dapat diakses oleh user dengan type yang ada di list types, contoh penggunaan: @type_required(types=[UserType.Admin, UserType.UMKM])
def type_required(types=[]):
    def inner(function):
        def wrapper(request, *args, **kwargs):
            if check_user_type(request.user) in types:
                return function(request, *args, **kwargs)
            return HttpResponse(status=404)
        return wrapper
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
    elif user.is_superuser:
        return UserType.Admin
    else:
        return None
    
def get_user_name(user):
    if check_user_type(user) == UserType.UMKM:
        return user.umkm.name
    return user.first_name + " " + user.last_name
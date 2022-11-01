from re import U
from django.contrib import admin
from .models import Customer, UMKM

# Register your models here.
admin.site.register(Customer)
admin.site.register(UMKM)
"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from general.views import landing_page, login_user, logout_user, register_user, register_type, register_umkm, register_customer, example_customer_only_page, example_umkm_only_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('showcase/', include('showcase.urls')),
    path('products/', include('products.urls')),
    path('obrolan/', include('obrolan.urls')),
    path('news/', include('news.urls')),
    path('lomba/', include('lomba.urls')),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register_user, name='register_user'),
    path('register-type/', register_type, name='register_type'),
    path('register-umkm/', register_umkm, name='register_umkm'),
    path('register-customer/', register_customer, name='register_customer'),
    path('test/umkm-only/', example_umkm_only_page, name='umkm-only'),
    path('test/customer-only/', example_customer_only_page, name='customer-only'),
]

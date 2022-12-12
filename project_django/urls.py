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
from general.views import *
from authentication.views import *

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
    path('api/get-user-id/', get_logged_in_user_id, name='get_logged_in_user_id'),
    path('api/login/', api_login, name='api_login'),
    path('api/logout/', api_logout, name='api_logout'),
    path('api/user-data/<int:user_id>/', api_user_data, name='api_user_data'),
    path('api/register/1/', api_register_one, name='api_register_one'),
    path('api/register/2/', api_register_two, name='api_register_two'),
    path('test/umkm-only/', example_umkm_only_page, name='umkm-only'),
    path('test/customer-only/', example_customer_only_page, name='customer-only'),
]

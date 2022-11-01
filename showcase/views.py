from itertools import product
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from showcase.models import Shop
from showcase.forms import ShopAddForm, RateForm
from general.models import UMKM, Customer
from general.utils import *
from general.constants import UserType
from products.models import Product


# Create your views here.
def show_showcase(request):
    data = Shop.objects.all()
    form = ShopAddForm()
    name = ""
    have_shop = 0
    userUMKM = (check_user_type(request.user) == UserType.UMKM)
    if userUMKM:
        umkm = UMKM.objects.get(user=request.user)
        have_shop = Shop.objects.filter(owner=umkm).count()
        name = umkm.name
    
    context = {
        "umkm":data,
        "user":request.user,
        "have_shop":have_shop,
        "isUMKM":userUMKM,
        "form":form,
        "name":name
    }
    return render(request, "showcase.html", context)

def show_shop(request, id):
    data = Shop.objects.get(pk=id)
    products = Product.objects.filter(owner=data.owner)
    rate = RateForm()
    name = ""
    userCust = (check_user_type(request.user) == UserType.Customer)
    if userCust:
        name = Customer.objects.get(user=request.user).first_name
    context = {
        "umkm":data,
        "products":products,
        "isCustomer":userCust,
        "rateForm":rate,
    }
    return render(request, "shop.html", context)


def show_json(request):
    data = Shop.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required
@umkm_required
def add_shop(request):
    form = ShopAddForm()

    if request.method == "POST":
        form = ShopAddForm(request.POST)
        if form.is_valid():
            form.save()
            data = {
                "fields":{
                    "shop_name":form.shop_name,
                    "umkm_url":form.umkm_url
                },
                "pk":form.pk
            }
            return JsonResponse(data)
    
@login_required
@customer_required
def rate_shop(request, id):
    form = RateForm()
    shop = Shop.objects.get(pk=id)

    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.rating_total
            shop.rating_count += 1
            shop.rating_total += rate
            shop.save()
            return JsonResponse(shop)
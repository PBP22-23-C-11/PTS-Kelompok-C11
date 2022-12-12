from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from showcase.models import Shop
from showcase.forms import ShopAddForm, RateForm
from general.models import UMKM, Customer
from general.utils import *
from general.constants import UserType

import json as JSON
from django.views.decorators.csrf import csrf_exempt


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
    rate = RateForm()
    name = ""
    userCust = (check_user_type(request.user) == UserType.Customer)
    if userCust:
        name = Customer.objects.get(user=request.user).first_name
    rating = data.rating_total/data.rating_count
    context = {
        "umkm":data,
        "isCustomer":userCust,
        "rateForm":rate,
        "name":name,
        "rate":rating
    }
    return render(request, "shop.html", context)


def show_json(request):
    data = Shop.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_shop(request):
    form = ShopAddForm()

    if request.method == "POST":
        form = ShopAddForm(request.POST)

        if form.is_valid():
            shop = Shop(owner=UMKM.objects.get(user=request.user),
                    shop_name=form.cleaned_data["shop_name"],
                    category=form.cleaned_data["category"],
                    description=form.cleaned_data["description"],
                    umkm_url=form.cleaned_data["umkm_url"],
                    number=form.cleaned_data["number"],
                    image=form.cleaned_data["image"])
            shop.save()
            data = {
                "fields":{
                    "shop_name":form.cleaned_data["shop_name"],
                    "umkm_url":form.cleaned_data["umkm_url"],
                    "category":form.cleaned_data["category"],
                    "image":form.cleaned_data["image"]
                },
                "pk":shop.pk
            }
            return JsonResponse(data)


@csrf_exempt
def add_shop_flutter(request):
    if request.method == "POST":
        form = JSON.loads(request.body)
    
        shop = Shop(owner=None,
                shop_name=form["shop_name"],
                category=form["category"],
                description=form["description"],
                umkm_url=form["umkm_url"],
                number=form["number"],
                image=form["image"])
        shop.save()

        return JsonResponse({"instance": "Success!"}, status=200)
    
@login_required
@customer_required
def rate_shop(request, id):
    form = RateForm()
    shop = Shop.objects.get(pk=id)

    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.cleaned_data["rating_total"]
            shop.rating_count += 1
            shop.rating_total += rate
            shop.save()

def rate_shop_flutter(request):
    if request.method == "POST":
        form = JSON.loads(request.body)
        shop = Shop.objects.get(pk=form["id"])

        shop.rating_count += 1
        shop.save()

        return JsonResponse({"instance": "Success!"}, status=200)
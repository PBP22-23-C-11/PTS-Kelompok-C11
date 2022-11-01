from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from showcase.models import Shop
from showcase.forms import ShopAddForm, RateForm
from general.models import UMKM, Customer
from general.utils import *
from general.constants import UserType


# Create your views here.
def show_showcase(request):
    data = Shop.objects.all()
    have_shop = Shop.objects.filter(owner=request.user).count()
    userUMKM = (check_user_type(request.user) == UserType.UMKM)
    userCust = (check_user_type(request.user) == UserType.Customer)
    form = ShopAddForm()
    rate = RateForm()
    context = {
        "umkm":data,
        "user":request.user,
        "have_shop":have_shop,
        "isUMKM":userUMKM,
        "isCust":userCust,
        "form":form,
        "rateForm":rate,
    }
    return render(request, "showcase.html", context)

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
            shop = Shop(
                user = request.user,
                shop_name = form.cleaned_data["shop_name"],
                description = form.cleaned_data["description"],
                umkm_url = form.cleaned_data["umkm_url"],
                number = form.cleaned_data["number"]
            )
            shop.save()
            data = {
                "fields":{
                    "shop_name":shop.shop_name,
                    "umkm_url":shop.umkm_url
                },
                "pk":shop.pk
            }
            return JsonResponse(data)
    
@login_required
@customer_required
def rate_shop(request, id):
    if request.method == "POST":
        data = Shop.objects.filter(pk=id)
        rate = request.POST.get("rate")
        temp = data.rating_total
        data.rating_total = temp + rate
        temp = data.rating_count
        data.rating_count = temp + 1
        data.save()
        return JsonResponse(data)
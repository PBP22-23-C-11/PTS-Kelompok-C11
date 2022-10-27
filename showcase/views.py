import imp
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from showcase.models import UMKM_Shop
from general.models import UMKM, Customer
from general.utils import umkm_required, customer_required, get_user_type
from general.constants import UserType


# Create your views here.
def show_showcase(request):
    data = UMKM_Shop.objects.all()
    userType = (get_user_type(request.user) == UserType.UMKM)
    context = {
        "umkm":data,
        "type":userType,
    }
    return render(request, "showcase.html")

def show_json(request):
    data = UMKM_Shop.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_ajax(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        umkm_url = request.POST.get("umkm_url")
        number = request.POST.get("number")
        umkm = UMKM_Shop.objects.create(shop_name=name,description=description,umkm_url=umkm_url,
            number=number,owner=request.user)
        data = {
            "fields":{
                "name":umkm.shop_name,
                "description":umkm.description,
                "umkm_url":umkm.umkm_url,
                "number":umkm.number,
            },
            "pk":umkm.pk
        }
        return JsonResponse(data)
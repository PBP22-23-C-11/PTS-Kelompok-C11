from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from django.core import serializers

from general.utils import *
from general.constants import *
from products.forms import AddProductForm
from products.models import Product

# Create your views here.
def show_products(request):
    form = AddProductForm()
    context = {'form' : form, 'is_UMKM' : check_user_type(request.user) == UserType.UMKM}
    return render(request, "products.html", context)

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            UMKM_name = form.cleaned_data['UMKM_name']
            product_name = form.cleaned_data['product_name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            owner = UMKM.objects.get(user = request.user)
                   
            product = Product.objects.create(UMKM_name=UMKM_name, product_name=product_name, price=price, description=description, owner=owner)

            products = {
                'pk' : product.pk,
                'fields' : {
                    'UMKM_name' : product.UMKM_name,
                    'product_name' : product.product_name,
                    'price' : product.price,
                    'description' : product.description,
                }
            }
            return JsonResponse(products)
        return HttpResponseBadRequest()
    
@csrf_exempt
def add_product_flutter(request):
    if request.method == 'POST':
        person = request.POST.get("UMKM")
        temp = User.objects.get(username=person)

        form = AddProductForm(request.POST)
        if form.is_valid():
            UMKM_name = form.cleaned_data['UMKM_name']
            product_name = form.cleaned_data['product_name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            owner = temp
                   
            product = Product.objects.create(UMKM_name=UMKM_name, product_name=product_name, price=price, description=description, owner=owner)

            products = {
                'pk' : product.pk,
                'fields' : {
                    'UMKM_name' : product.UMKM_name,
                    'product_name' : product.product_name,
                    'price' : product.price,
                    'description' : product.description,
                }
            }
            return JsonResponse(products)
        return HttpResponseBadRequest()

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
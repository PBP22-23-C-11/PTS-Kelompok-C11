from django.shortcuts import redirect, render
from django.contrib import messages

from general.utils import *
from products.models import Product

# Create your views here.
def show_products(request):
    products = Product.objects.all()
    type = check_user_type(request.user)
    context = {'products' : products, 'type' : type}
    return render(request, "products.html", context)

def add_product(request):
    if request.method == 'POST':
        product = Product()
        product.UMKM_name = request.POST.get('UMKM_name')
        product.product_name = request.POST.get('product_name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.save()
        messages.succes(request, "Product has beed added succesfully!")
    return redirect('products : show_products')
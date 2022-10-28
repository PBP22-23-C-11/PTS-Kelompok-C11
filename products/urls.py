from django.urls import path
from products.views import show_products
from products.views import add_product

app_name = 'products'

urlpatterns = [
    path('', show_products, name='show_products'),
    path('add/', add_product, name='add_product'),
]
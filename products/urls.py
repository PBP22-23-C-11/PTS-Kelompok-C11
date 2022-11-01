from django.urls import path
from products.views import show_products
from products.views import add_product
from products.views import show_json

app_name = 'products'

urlpatterns = [
    path('', show_products, name='show_products'),
    path('add/', add_product, name='add_product'),
    path('json/', show_json, name='show_json'),
]
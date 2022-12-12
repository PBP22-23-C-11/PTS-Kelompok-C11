from django.urls import path
from showcase.views import *

app_name = 'showcase'

urlpatterns = [
    path('', show_showcase, name='show_showcase'),
    path('shop/<int:id>', show_shop, name="show_shop"),
    path('json/', show_json, name="show_json"),

    path('add_shop/', add_shop, name="add_shop"),
    path('add_shop_flutter/', add_shop_flutter, name="add_shop_flutter"),
    
    path('rate_shop/<int:id>', rate_shop, name="rate_shop"),
    path('rate_shop_flutter/', rate_shop_flutter, name="rate_shop_flutter")
]
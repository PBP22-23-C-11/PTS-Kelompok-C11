from django.urls import path
from showcase.views import *

app_name = 'showcase'

urlpatterns = [
    path('', show_showcase, name='show_showcase'),
    path('json', show_json, name="show_json"),
    path('add_shop/', add_shop, name="add_shop"),
    path('rate_shop/', rate_shop, name="rate_shop"),
]
from django.urls import path
from showcase.views import *

app_name = 'showcase'

urlpatterns = [
    path('', show_showcase, name='show_showcase'),
    path('json', show_json, name="show_json"),
    path('add_ajax/', add_ajax, name="add_ajax"),
]
from django.urls import path
from showcase.views import show_showcase

app_name = 'showcase'

urlpatterns = [
    path('', show_showcase, name='show_showcase'),
]
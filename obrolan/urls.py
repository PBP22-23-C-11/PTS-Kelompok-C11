from django.urls import path
from obrolan.views import show_obrolan

app_name = 'obrolan'

urlpatterns = [
    path('', show_obrolan, name='show_obrolan'),
]
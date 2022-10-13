from django.urls import path
from lomba.views import show_lomba

app_name = 'lomba'

urlpatterns = [
    path('', show_lomba, name='show_lomba'),
]
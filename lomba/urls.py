from django.urls import path
from lomba.views import *

app_name = 'lomba'

urlpatterns = [
    path('', show_lomba, name='show_lomba'),
    path('buat/', buat_lomba, name='buat_lomba'),
    path('vote/<int:id>', vote_lomba, name='vote_lomba'),
    path('daftar/<int:id>', daftar_lomba, name='daftar_lomba'),
    path('all/', all_lomba, name='all_lomba'),
    path('all/data/<int:id>', data_lomba, name='data_lomba'),
    path('all/data/json', all_lomba_json, name='all_lomba_json'),
]
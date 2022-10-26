from django.urls import path
from lomba.views import show_lomba, daftar_lomba, vote_lomba, buat_lomba

app_name = 'lomba'

urlpatterns = [
    path('', show_lomba, name='show_lomba'),
    path('buat/', buat_lomba, name='buat_lomba'),
    path('vote/', vote_lomba, name='vote_lomba'),
    path('daftar/', daftar_lomba, name='daftar_lomba'),
]
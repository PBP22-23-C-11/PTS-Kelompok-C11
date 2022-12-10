from django.urls import path
from obrolan.views import create_diskusi_ajax, create_diskusi_flutter, delete_disc, show_obrolan, show_diskusi_json

app_name = 'obrolan'

urlpatterns = [
    path('', show_obrolan, name='show_obrolan'),
    path('add/', create_diskusi_ajax, name='create_diskusi_ajax'),
    path('json/', show_diskusi_json, name='show_diskusi_json'),
    path('delete-disc/<int:id>/', delete_disc, name='delete-disc'),
    path('add-disc-flutter', create_diskusi_flutter, name='create_diskusi_flutter'),
]
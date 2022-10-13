from django.urls import path
from news.views import show_news

app_name = 'news'

urlpatterns = [
    path('', show_news, name='show_news'),
]
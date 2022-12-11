from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path('', news_page_umkm, name='news_page_umkm'),
    path('official/', news_page_official, name='news_page_official'),
    path('subscribed/', news_page_subscribed, name='news_page_subscribed'),
    path('api/article/', article, name='article'),
    path('<int:article_id>/', article_page, name='article_page'),
    path('api/articles/<int:article_id>/', article_by_id, name='article_by_id'),
    path('api/articles/<int:article_id>/comments/', article_comments, name='article_comments'),
    path('api/articles/<int:article_id>/comments/<int:comment_id>/', article_comment_by_id, name='article_comment_by_id'),
    path('api/articles/<int:article_id>/comments/<int:comment_id>/delete/', delete_article_comment_by_id_get, name='delete_article_comment_by_id_get'),
    path('api/articles/<int:article_id>/likes/', like, name='like'),
    path('api/articles/<int:article_id>/likes/toggle/', toggle_like_get, name='toggle_like_get'),
    path('api/articles/<int:article_id>/delete/', delete_article_by_id_get, name='delete_article_by_id_get'),
    path('api/subscribes/<int:author_id>/', subscribe, name='subscribe'),
    path('api/subscribes/<int:author_id>/toggle/', toggle_subscribe_get, name='toggle_subscribe_get'),
]
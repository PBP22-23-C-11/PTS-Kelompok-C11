from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from general.models import UMKM, Customer

# Create your models here.
class Article(models.Model):
    author_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    image = models.URLField(null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField()

class OfficialArticle(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE)

class UMKMArticle(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    author_umkm = models.ForeignKey(UMKM, null=True, on_delete=models.CASCADE)

class Like(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())

class Subscribe(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
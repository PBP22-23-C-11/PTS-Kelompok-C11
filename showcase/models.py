from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    umkm_url = models.URLField(default="")
    number = models.CharField(max_length=13, default="")
    rating_total = models.IntegerField(default=5)
    rating_count = models.IntegerField(default=1)
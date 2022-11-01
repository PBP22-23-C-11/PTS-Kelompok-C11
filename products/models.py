from django.db import models
from django.conf import settings
from general.models import UMKM
from django.contrib.auth.models import User

# Create your models here
class Product(models.Model):
    UMKM_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    owner = models.ForeignKey(UMKM, on_delete=models.CASCADE) # Satu UMKM bisa memiliki banyak product

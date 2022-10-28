from django.db import models
from django.contrib.auth.models import User
from general.models import UMKM

# Create your models here
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # Satu UMKM bisa memiliki banyak product
    UMKM_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
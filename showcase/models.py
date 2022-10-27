from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from general.models import UMKM


# Create your models here.
class UMKM_Shop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255, default=owner.name)
    description = models.TextField(default="")
    umkm_url = models.URLField(default="")
    number = models.CharField(max_length=13, default="")
    rating_total = models.FloatField(default=5.0)
    rating_count = models.IntegerField(default=1)
    
    def __str__(self): # return rating of shop
        return "%f" % self.rating_total/self.rating_count
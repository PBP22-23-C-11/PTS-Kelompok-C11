from django.db import models
from general.models import UMKM
from showcase.choices import CATEGORY_CHOICES

# Create your models here.
class Shop(models.Model):
    owner = models.OneToOneField(UMKM, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255, default="")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=18, default="other")
    description = models.TextField(default="")
    umkm_url = models.URLField(default="")
    number = models.CharField(max_length=13, default="")
    image = models.URLField(null=True)
    rating_total = models.IntegerField(default=5)
    rating_count = models.IntegerField(default=1)
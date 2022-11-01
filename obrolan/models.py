from django.db import models
from django.conf import settings
from datetime import timedelta

# Create your models here.
class Diskusi(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=250)
    date = models.DateTimeField()
    title = models.CharField(max_length=250)
    toWho = models.CharField(max_length=250)
    message = models.TextField()
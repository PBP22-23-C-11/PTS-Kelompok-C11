from django.db import models
from general.models import UMKM, Customer

# Create your models here.

# Model untuk lombanya
class Lomba(models.Model):
    id_lomba = models.IntegerField()
    keterangan = models.TextField()

# Model untuk UMKM yang ikut lomba
class DetailLomba(models.Model):
    lomba = models.OneToOneField(Lomba, on_delete = models.CASCADE)
    peserta = models.OneToOneField(UMKM, on_delete = models.CASCADE)
    detailKeterangan = models.TextField()

# Model untuk cek apakah Customer sudah voting
class Voting(models.Model):
    pemilih = models.OneToOneField(Customer, on_delete = models.CASCADE)
    lomba = models.OneToOneField(Lomba, on_delete = models.CASCADE)
    cekPemilihan = models.BooleanField(default=False)
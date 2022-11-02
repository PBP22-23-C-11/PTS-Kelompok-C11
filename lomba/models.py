from django.db import models
from general.models import UMKM, Customer
from django.contrib.auth.models import User

# Create your models here.

# Model untuk lombanya
class Lomba(models.Model):
    namaLomba = models.TextField()
    keterangan = models.TextField()
    tanggal = models.DateField(auto_now=True)
    berjalan = models.BooleanField(default=True)

# Model untuk UMKM yang ikut lomba
class DetailLomba(models.Model):
    lomba = models.ForeignKey(Lomba, on_delete = models.CASCADE)
    peserta = models.ForeignKey(User, on_delete = models.CASCADE)
    namaKarya = models.CharField(max_length=50)
    detailKeterangan = models.TextField()
    situsKarya = models.TextField()
    jumlahVote = models.IntegerField(default=0)

# Model untuk cek apakah Customer sudah voting
class Voting(models.Model):
    pemilih = models.ForeignKey(User, on_delete = models.CASCADE)
    lomba = models.ForeignKey(Lomba, on_delete = models.CASCADE)
from difflib import context_diff
from subprocess import DETACHED_PROCESS
from django.shortcuts import render
from django.http import HttpResponse
from general.utils import *
from lomba.models import DetailLomba, Lomba, Voting
from django.core import serializers

# Create your views here.
def show_lomba(request):
    check = check_user_type(request.user)
    context = {
        'user': request.user,
        'check': check,
    }
    return render(request, "lomba.html", context)

# Khusus admin selesai
# Tinggal perbaiki template
@admin_required
def buat_lomba(request):
    if request.method == 'POST':
        lomba = Lomba()
        lomba.namaLomba = request.POST.get('name')
        lomba.keterangan = request.POST.get('keterangan')
        lomba.save()
        return redirect('lomba:show_lomba')

    return render(request, 'buatlomba.html')

# Khusus UMKM selesai
# Tinggal perbaiki template
# id dari lomba yg ingin didaftarkan
def daftar_lomba(request, id):
    if request.method == 'POST':
        daftarLomba = DetailLomba()
        daftarLomba.lomba = Lomba.objects.get(id=id)
        daftarLomba.peserta = request.user
        daftarLomba.namaKarya = request.POST.get('nama-karya')
        daftarLomba.detailKeterangan = request.POST.get('keterangan')
        daftarLomba.situsKarya = request.POST.get('situs-karya')
        daftarLomba.save()
        return redirect('lomba:show_lomba')
    
    lomba = Lomba.objects.get(id=id)
    context = {
        'lomba': lomba,
    }
    return render(request, 'halamandaftar.html', context)

# Khusus Customer
# Blom jadi
# idnya dari lomba
# Model salah dikit
def vote_lomba(request, id):
    if request.method == 'POST':
        pemilih = Voting()
        pemilih.pemilih = request.user
        pemilih.lomba = Lomba.objects.get(id=id)
        pemilih.save()

        lomba = DetailLomba.objects.get(lomba = pemilih.lomba)
        lomba.jumlahVote += 1
        lomba.save()

        return redirect('lomba:vote_lomba')
    return render(request, "halamanvoting.html")

# Ubah pakai ajax aja selesai
def all_lomba(request):
    context = {}
    return render(request, 'halamandata.html', context)

# return objeck lomba ke json selesai
# sudah benar
def all_lomba_json(request):
    allLomba = Lomba.objects.all()
    return HttpResponse(serializers.serialize("json", allLomba), content_type="application/json")

# id berupa id Lomba
def data_lomba(request, id):
    lomba = Lomba.objects.get(id=id)
    detail = DetailLomba.objects.filter(lomba=lomba)
    check = check_user_type(request.user)
    context = {
        'check': check,
        'detail': detail,
    }
    return render(request, 'dataspes.html',context)
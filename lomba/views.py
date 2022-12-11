import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from general.utils import *
from lomba.models import DetailLomba, Lomba, Voting
from django.core import serializers
from lomba.forms import LombaForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Halaman utama lomba
def show_lomba(request):
    check = check_user_type(request.user)
    login = "No data"

    if request.user.is_authenticated:
        if request.COOKIES.get('last_login', 'default') != 'default':
            login = request.COOKIES['last_login']

    context = {
        'user': request.user,
        'check': check,
        'last_login': login,
    }
    return render(request, "lomba.html", context)

# Untuk membuat lomba baru (khusus admin)
# @login_required(login_url='/login')
# @admin_required
@csrf_exempt
def buat_lomba(request):
    form = LombaForm()

    if request.method == 'POST':
        form = LombaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('lomba:all_lomba')

    context = { 'form': form }
    return render(request, 'buatlomba.html', context)

# Untuk mendaftar pada suatu lomba (khusus UMKM)
# id berasal dari Lomba yang ingin didaftarkan
@login_required(login_url='/login')
@umkm_required
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
    cekPendaftaran = len(DetailLomba.objects.all().filter(lomba=lomba, peserta=request.user));
    context = {
        'lomba': lomba,
        'cekDaftar': cekPendaftaran,
        'cekOng': lomba.berjalan,
    }
    return render(request, 'halamandaftar.html', context)

# id berasal dari Lomba yang ingin didaftarkan
@csrf_exempt
def daftar_lomba_flutter(request, id):
    if request.method == 'POST':
        person = request.POST.get('umkm')
        temp = User.objects.get(username=person)   # Ambil data user UMKM

        try:
            cekDaftar = DetailLomba.objects.get(peserta=temp, lomba=Lomba.objects.get(id=id))

            return HttpResponse("gagal", content_type="text/plain")

        except:
            daftarLomba = DetailLomba()
            daftarLomba.lomba = Lomba.objects.get(id=id)
            daftarLomba.peserta = temp
            daftarLomba.namaKarya = request.POST.get('nama-karya')
            daftarLomba.detailKeterangan = request.POST.get('keterangan')
            daftarLomba.situsKarya = request.POST.get('situs-karya')
            daftarLomba.save()

            return HttpResponse("berhasil", content_type="text/plain")
        

# Untuk memberikan suara pada peserta lomba (khusus Customer)
# id berasal dari DetailLomba (id peserta lomba)
# @login_required(login_url='/login')
# @customer_required
@csrf_exempt
def vote_lomba(request, id):
    if request.method == 'POST':
        dataLomba = DetailLomba.objects.get(id=id)
        dataLomba.jumlahVote += 1
        dataLomba.save()

        pemilih = Voting()
        pemilih.pemilih = request.user
        pemilih.lomba = dataLomba.lomba
        pemilih.save()

        return redirect('lomba:all_lomba')

@csrf_exempt
def vote_flutter(request, id):
    if request.method == 'POST':
        dataLomba = DetailLomba.objects.get(id=id)
        person = request.POST.get('customer')
        temp = User.objects.get(username=person)

        try:
            voting = Voting.objects.get(pemilih=temp, lomba=dataLomba.lomba)
            return HttpResponse("gagal", content_type="text/plain")

        except:
            dataLomba.jumlahVote += 1
            dataLomba.save()

            pemilih = Voting()
            pemilih.pemilih = temp
            pemilih.lomba = dataLomba.lomba
            pemilih.save()

            return HttpResponse("berhasil", content_type="text/plain")

# Untuk menampilkan data semua lomba
def all_lomba(request):
    context = {
        'check': check_user_type(request.user),
    }
    return render(request, 'halamandata.html', context)

# Kembalikan objek lomba menjadi JSON
def all_lomba_json(request):
    allLomba = Lomba.objects.all()
    return HttpResponse(serializers.serialize("json", allLomba), content_type="application/json")

# Ambil data peserta lomba (DetailLomba) melalui id-nya
# ubah menjadi bentuk JSON
def peserta_lomba_json(request, id):
    pesertaLomba = DetailLomba.objects.all().filter(id=id)
    return HttpResponse(serializers.serialize("json", pesertaLomba), content_type="application/json")

# Ambil peserta suatu lomba
def peserta_lomba(request, id):
    lomba = Lomba.objects.get(id=id)
    detail = DetailLomba.objects.filter(lomba=lomba)
    return HttpResponse(serializers.serialize("json", detail), content_type="application/json")

# Tampilkan seluruh data peserta lomba
# id berasal dari Lomba
def data_lomba(request, id):
    lomba = Lomba.objects.get(id=id)
    detail = DetailLomba.objects.filter(lomba=lomba)
    jumlah = len(detail)
    diPilih = 0
    check = 99

    # Jika user sedang login
    if request.user.is_authenticated:
        diPilih = len(Voting.objects.filter(pemilih=request.user, lomba=lomba))
        check = check_user_type(request.user)

    context = {
        'check': check,
        'detail': detail,
        'id': id,
        'sudahPilih': diPilih,
        'lomba': lomba,
        'ongoing': lomba.berjalan,
        'jumlahPeserta': jumlah,
    }
    return render(request, 'dataspes.html', context)

# Id berasal dari Lomba
def update_lomba(request, id):
    lomba = Lomba.objects.get(id=id)

    if lomba.berjalan == True:
        lomba.berjalan = False
  
    lomba.save()
    return redirect('lomba:all_lomba')
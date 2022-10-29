from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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
@login_required(login_url='/login')
@admin_required
def buat_lomba(request):
    if request.method == 'POST':
        lomba = Lomba()
        lomba.namaLomba = request.POST.get('name')
        lomba.keterangan = request.POST.get('keterangan')
        lomba.save()
        return redirect('lomba:all_lomba')

    return render(request, 'buatlomba.html')

# Khusus UMKM
# id dari lomba yg ingin didaftarkan
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
    }
    return render(request, 'halamandaftar.html', context)

# Khusus Customer
# idnya dari detailLomba
@login_required(login_url='/login')
@customer_required
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

# Tampilkan lomba
def all_lomba(request):
    return render(request, 'halamandata.html')

# Return objek lomba menjadi json
def all_lomba_json(request):
    allLomba = Lomba.objects.all()
    return HttpResponse(serializers.serialize("json", allLomba), content_type="application/json")

# Id pake detaillomba
# hasilin json buat ubah nilainya doang
def peserta_lomba_json(request, id):
    pesertaLomba = DetailLomba.objects.all().filter(id=id)
    return HttpResponse(serializers.serialize("json", pesertaLomba), content_type="application/json")

# id berupa id Lomba
# Tampilkan seluruh data peserta pada lomba
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
        'jumlahPeserta': jumlah,
    }
    return render(request, 'dataspes.html', context)

# Hanya test
def test(request):
    return redirect('/lomba/')
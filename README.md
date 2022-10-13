## buzzar-id
Sebuah wadah bagi para pemilik UMKM dan pelanggan untuk berinteraksi dan mengenal karya wirausaha.<br> 
Proyek ini dibuat untuk memenuhi Proyek Tugas Tengah Semester mata kuliah Pemrograman Berbasis Plaform oleh Fakultas Ilmu Komputer Universitas Indonesia pada Tahun Ajaran 2022/2023 

#### Anggota Kelompok
Proyek ini dibuat oleh kelompok C-11 yang beranggotakan:
1. Ahmad Hanif Adisetya (2106750603)
2. Emir Shamsuddin Fadhlurrahman (2106632541)
3. Kevin Alexander (2106705026)
4. Muhammad Nabiel Andityo Purnomo (2106750465)
5. Vania Azria Wardani (2106650380)

#### Link Aplikasi Heroku
https://buzzar-id.herokuapp.com/

#### Overview
Forum G20 merupakan forum kerja sama multilateral yang terdiri dari 19 negara utama dan Uni Eropa. G20 dibentuk pada 1999 atas inisiasi anggota G7. Forum G20 merangkul negara maju dan berkembang untuk bersama-sama mengatasi krisis dan bertujuan mewujudkan pertumbuhan global yang kuat, berkelanjutan, seimbang, dan inklusif. Pada tahun 2022, Indonesia memegang presidensi G20. Tema Presidensi G20 Indonesia 2022 yang diusung adalah *Recover Together, Recover Stronger*. Dengan tema tersebut, Indonesia mengajak seluruh dunia untuk saling mendukung pulih bersama serta tumbuh lebih kuat dan berkelanjutan. 
<br><br>
Salah satu isu utama yang diusung pada G20 tahun ini adalah **Transformasi Digital**. Menerapkan digitalisasi terhadap tatanan ekonomi dapat memulihkannya serta menjadi lebih kuat, inklusif dan kolaboratif. Salah satu kunci dalam pemulihan tatanan ekonomi adalah dengan pemberdayaan UMKM untuk mengakselerasikannya. Kelompok kami mencoba untuk memperdayakan hal tersebut, maka kami usung web aplikasi yang bernama **buzzar**.
<br><br>
Fitur utamanya tentu saja adalah adanya kumpulan UMKM yang telah memiliki cabang digital di tempat lain dan tidak menutup kemungkinan juga UMKM yang belum memiliki cabang digital dapat bergabung.
<br><br>
Selain itu terdapat juga fitur news untuk menampilkan berbagai informasi menarik yang dapat diisi oleh UMKM, seperti promosi, informasi, dan hal-hal lainnya.
<br><br>
Fitur lainnya yang tidak kalah penting adalah Obrolan UMKM. Pada fitur ini, pengguna dapat berbincang dengan pemilik UMKM, hal yang biasanya sulit dilakukan karena biasanya pemilik UMKM tidak menyediakan layanan secara daring.
<br><br>
Dengan adanya situs web ini, kami ingin masyarakat umum dapat lebih mudah dalam pencarian UMKM beserta informasi-informasinya sehingga UMKM-UMKM tersebut dapat berkembang dengan lebih baik.

#### Daftar Modul
Berikut adalah daftar modul yang akan kami implementasikan.
1. News: Menampilkan informasi dari berbagai UMKM dan Admin (Maintenance, lomba, dsb.). Pengguna dapat melakukan _filter_ berdasarkan UMKM, kategori, dsb. Pengguna juga dapat melakukan _subscribe_ pada beberapa UMKM dan dapat melakukan _filter_ pada news sedemikian sehingga hanya UMKM yang di-_subscribe_-lah yang dapat dilihat.

2. Showcase: Menampilkan daftar UMKM. Kita bisa melakukan _filter_ dan _sort_. Ketika UMKM diklik, data dari UMKM yang diklik akan ditampilkan. Data tersebut contohnya adalah nama, sebagian produk, dll.

3. Products: Menampilkan produck-produk. Bisa di-_filter_ untuk seluruh UMKM atau UMKM spesifik. Redirect ke shoppee, tokopedia, etc. (multi-toko)

4. Lomba -> Tiap bulan ada program dimana tiap umkm bisa berlomba2 jadi yang terbaik -> Hadiah Modal usaha, showcase top umkm per bulan

5. Obrolan UMKM -> Pengguna bisa ngobrol2 dengan pemilik UMKM

#### Peran Pengguna
Pengguna yang login dibagi menjadi 2, pemilik UMKM dan pengguna/customer.

- UMKM
Memiliki semua basic features dengan tambahan:
1) Menambahkan UMKM pada saat registrasi (Untuk showcase & lomba)
2) Menambahkan produk yang dia miliki (Untuk products & lomba)
3) Bisa melihat lomba & menambahkan, namun tidak bisa vote
4) Bisa menambah obrolan pada obrolan UMKM
<br>

- Pengguna/customer
Memiliki semua basic features dengan tambahan:
1) Bisa akses dan melakukan vote di bagian lomba
2) Bisa menambah obrolan pada obrolan UMKM
<br>

- Pengguna tidak login
Hanya memiliki basic features:
1) Bisa melihat news dengan tambahan 2 subseksi yaitu news utama dan news dari admin
2) Melihat showcase
3) Melihat products 

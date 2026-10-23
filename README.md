# Pertemuan 10 - String dan Pengolahan Teks

Nama: Indri Meilani
NIM: 2225250141
Kelas: 3A

## Tujuan
Mengolah dan menormalisasi data teks dengan string Python.

## Cara Menjalankan
python3 tugas/normalisasi_data_mahasiswa.py

## Algoritma
Proses normalisasi basis data pada dasarnya adalah langkah-langkah sistematis untuk merapikan tabel-tabel data dengan cara memecah atau mengelompokkannya, sehingga tidak ada informasi yang berulang (redundansi) dan struktur data menjadi lebih efisien serta konsisten. Tujuannya adalah untuk menghindari anomali saat kita menambah, mengubah, atau menghapus data, sehingga integritas dan kualitas database tetap terjaga dengan baik.

## Test Case
Berdasarkan pengujian fungsionalitas program, pengujian pertama dengan input "aan hendrayana pmat a 2026" menghasilkan keluaran aktual "Aan Hendrayana | PMAT-A-2026 | AH" yang sesuai dengan hasil yang diharapkan dengan status Lulus (Berhasil); pengujian kedua dengan input "fATHIYYAH mUTHMAINNAH kelas b" menghasilkan "Fathiyyah Muthmainnah | KELAS-B | FM" dengan status Lulus; pengujian ketiga dengan input "BUDI pmtk 01" memberikan hasil "Budi | PMTK-01 | B" berstatus Lulus; serta pengujian keempat dengan input "siti nur aisyah kelas c" sukses mengeluarkan "Siti Nur Aisyah | KELAS-C | SNA" dengan status Lulus, yang menandakan seluruh sistem pemrosesan teks, kapitalisasi, dan pembentukan kode inisial bekerja dengan sempurna sesuai ekspektasi.

## Refleksi
Salah satu masalah teks utama yang ditemukan dalam pengolahan data tersebut adalah ketidakkonsistenan huruf besar dan kecil yang tercampur secara acak (seperti pada "fATHIYYAH mUTHMAINNAH kelas b") serta variasi spasi yang tidak beraturan pada input pengguna. Masalah ini diperbaiki pada bagian kode dengan menerapkan fungsi manipulasi string secara bertahap, yaitu mengubah format nama menjadi title case agar setiap awal kata berhuruf kapital, mengubah bagian kode atau kelas menjadi huruf kapital penuh (uppercase), serta melakukan pemisahan kata (splitting) berdasarkan spasi untuk mengekstrak inisial nama secara akurat, sehingga keluaran akhir teks menjadi seragam, bersih, dan terstruktur dengan rapi.

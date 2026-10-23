def normalisasi_nama(nama):
    # Mengubah setiap kata menjadi huruf kapital di awal (Title Case)
    return nama.strip().title()

def buat_inisial(nama):
    # Mengambil huruf pertama dari setiap kata, lalu menjadikannya huruf besar
    words = nama.strip().split()
    return "".join([w[0].upper() for w in words if w])

def normalisasi_kode(kode):
    # Memisahkan berdasarkan spasi, mengubah ke huruf besar, lalu menggabungkannya dengan tanda hubung (-)
    return "-".join(kode.strip().split()).upper()

# Program utama
nama = input("Nama: ")
kode = input("Kode kelas: ")

# Memproses hasil
hasil_nama = normalisasi_nama(nama)
hasil_kode = normalisasi_kode(kode)
hasil_inisial = buat_inisial(nama)

# Menampilkan hasil sesuai format yang diminta
print(f"{hasil_nama} | {hasil_kode} | {hasil_inisial}")
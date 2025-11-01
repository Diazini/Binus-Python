usia = int(input("Masukkan usia Anda: "))

if usia < 0:
    print("Usia tidak boleh negatif.")
elif usia <= 1:
    kategori = "Bayi"
elif usia <= 3:
    kategori = "Balita"
elif usia <= 5:
    kategori = "Anak Prasekolah"
elif usia <= 12:
    kategori = "Anak"
elif usia <= 17:
    kategori = "Remaja"
elif usia <= 21:
    kategori = "Dewasa Muda"
elif usia <= 30:
    kategori = "Pra-dewasa"
elif usia <= 50:
    kategori = "Dewasa"
elif usia <= 70:
    kategori = "Pra-lansia"
else:
    kategori = "Lansia"
if usia >= 0:
    print(f"Kategori usia Anda adalah: {kategori}")

print("=== Konversi Suhu ===")
print("1. Celsius ke Fahrenheit")
print("2. Celsius ke Kelvin")
print("3. Fahrenheit ke Celsius")
print("4. Fahrenheit ke Kelvin")
print("5. Kelvin ke Celsius")
print("6. Kelvin ke Fahrenheit")

pilihan = int(input("Masukkan pilihan (1-6): "))
suhu = int(input("Masukkan suhu: "))

if pilihan == 1:
    hasil = (suhu * 9/5) + 32
    satuan_awal = "Celsius"
    satuan_akhir = "Fahrenheit"
elif pilihan == 2:
    hasil = suhu + 273.15
    satuan_awal = "Celsius"
    satuan_akhir = "Kelvin"
elif pilihan == 3:
    hasil = (suhu - 32) * 5/9
    satuan_awal = "Fahrenheit"
    satuan_akhir = "Celsius"
elif pilihan == 4:
    hasil = (suhu - 32) * 5/9 + 273.15
    satuan_awal = "Fahrenheit"
    satuan_akhir = "Kelvin"
elif pilihan == 5:
    hasil = suhu - 273.15
    satuan_awal = "Kelvin"
    satuan_akhir = "Celsius"
elif pilihan == 6:
    hasil = (suhu - 273.15) * 9/5 + 32
    satuan_awal = "Kelvin"
    satuan_akhir = "Fahrenheit"
else:
    print("Pilihan tidak valid.")

print(f"\n{suhu:.2f} derajat {satuan_awal} = {hasil:.2f} derajat {satuan_akhir}")

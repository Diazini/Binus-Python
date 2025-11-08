while True:
    angka = input("Masukkan angka apa pun: ")

    if not angka.isdigit():
        print("Harap masukkan angka yang valid!")
        continue

    angka = int(angka)

    if angka % 2 == 0:
        print(f"Angka {angka} genap.")
    else:
        print(f"Angka {angka} ganjil.")

    ulang = input("Ingin mengulang? (Y/N): ")
    if ulang != 'Y':
        print("Program Berhenti")
        print("Terima kasih telah menggunakan program saya ^^")

class Data:
    def __init__(self, nama="-", nilai="-"):
        self._name = nama
        self._nilai = nilai

    def get_name(self):
        return self._name

    def set_name(self, nama_baru):
        self._name = nama_baru

    def get_nilai(self):
        return self._nilai

    def set_nilai(self, nilai_baru):
        try:
            self._nilai = float(nilai_baru)
        except ValueError:
            print("Nilai harus angka.")


def main():
    item = "-"  # tanda untuk data kosong

    while True:
        print("===== MENU DATA =====")
        print("1.Tambah Data")
        print("2.Tampilkan Data")
        print("3.Ubah Data")
        print("4.Hapus Data")
        print("5.Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == "1":
            nama = input("Masukkan nama: ")
            nilai = input("Masukkan nilai: ")
            item = Data(nama, nilai)
            print("Data Berhasil Ditambahkan")

        elif pilihan == "2":
            if item == "-":
                print("Nama  : Tidak ada")
                print("Nilai : Tidak ada")
            else:
                print("Nama  :", item.get_name())
                print("Nilai :", item.get_nilai())

        elif pilihan == "3":
            if item == "-":
                print("Data Belum Diubah")
            else:
                print("Pilih yang ingin diubah:")
                print("a. Nama")
                print("b. Nilai")
                sub = input("Masukkan pilihan (a/b): ").lower()
                if sub == "a":
                    nama_baru = input("Masukkan nama baru: ")
                    item.set_name(nama_baru)
                    print("Nama Berhasil Diubah")
                elif sub == "b":
                    nilai_baru = input("Masukkan nilai baru: ")
                    item.set_nilai(nilai_baru)
                    print("Nilai Berhasil Diubah")
                else:
                    print("Pilihan tidak valid")

        elif pilihan == "4":
            item = "-"
            print("Data Berhasil Dihapus")

        elif pilihan == "5":
            print("Program Selesai. Terima Kasih!")
            break

        else:
            print("Pilihan tidak valid")

        print()


if __name__ == "__main__":
    main()

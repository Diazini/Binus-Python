maks = int(input("Masukkan nilai maksimum : "))
if maks > 0:
    for i in range(maks, 0, -1):
        print(str(i) * i)

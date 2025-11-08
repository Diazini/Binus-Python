temp = 0
rerata = 0

while (True):
    nilai = input("Masukkan Nilai : ")
    if (nilai == ""):
        rerata = rerata/temp
        print(rerata)
        break
    elif (nilai == "A"):
        rerata = rerata + 4.00
        temp = temp + 1
    elif (nilai == "-A"):
        rerata = rerata + 3.75
        temp = temp + 1
    elif (nilai == "B+"):
        rerata = rerata + 3.50
        temp = temp + 1
    elif (nilai == "B"):
        rerata = rerata + 3.00
        temp = temp + 1
    elif (nilai == "B-"):
        rerata = rerata + 2.75
        temp = temp + 1
    elif (nilai == "C+"):
        rerata = rerata + 2.50
        temp = temp + 1
    elif (nilai == "C"):
        rerata = rerata + 2.00
        temp = temp + 1
    elif (nilai == "C-"):
        rerata = rerata = 1.75
        temp = temp + 1
    elif (nilai == "D"):
        rerata = rerata + 2.50
        temp = temp + 1
    elif (nilai == "E"):
        rerata = rerata + 1.20
        temp = temp + 1

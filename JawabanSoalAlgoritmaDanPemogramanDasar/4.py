def rerata_nilai_mhs(nama, dataDict):

    nilai_list = dataDict[nama]


    for nilai in nilai_list:
        print(nilai, end=" ")
    print()       

    rerata = sum(nilai_list) / len(nilai_list)
    print("Rerata =", int(rerata))

dataDict = {
    'Icha': [80, 70, 70, 80]
}
rerata_nilai_mhs('Icha', dataDict)

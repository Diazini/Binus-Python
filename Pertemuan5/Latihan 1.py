
def addition(value1 =0, value2 =0):
    return value1 + value2
    
def subtraction(value1 =0, value2 =0):
    return value1 - value2
    
def division(value1 =0, value2 =0):
    return value1 / value2
    
def multiplication(value1 =0, value2 =0):
    return value1 * value2
    
def modulus(value1 =0, value2 =0):
    return value1 % value2



def banner():
    print("""
    Muhammad Diaz Anugrah 
    Kebayoran Lama""")

banner()

while(True):
    menu = input("Enter Menu (+|-|/|*|%|stop): ")
    
    if (menu == "stop"):
        print("Terimkasih telah menggunakan program")
        break;
        
    elif (menu == "+"):
        value1= int(input("Masukkan Nilai1: "))
        value2= int(input("Masukkan Nilai2: "))
        hasil = addition(value1, value2)
        print("The result of addition", value1, "+", value2, "is",hasil)
        
    elif (menu == "-"):
        value1= int(input("Masukkan Nilai1: "))
        value2= int(input("Masukkan Nilai2: "))
        hasil = subtraction(value1, value2)
        print("The result of subtraction", value1, "-", value2, "is",hasil)
        
    elif (menu == "/"):
        value1= int(input("Masukkan Nilai1: "))
        value2= int(input("Masukkan Nilai2: "))
        hasil = division(value1, value2)
        print("The result of division", value1, "/", value2, "is",hasil)
        
    elif (menu == "*"):
        value1= int(input("Masukkan Nilai1: "))
        value2= int(input("Masukkan Nilai2: "))
        hasil = multiplication(value1, value2)
        print("The result of multiplication", value1, "*", value2, "is",hasil)
        
    elif (menu == "%"):
        value1= int(input("Masukkan Nilai1: "))
        value2= int(input("Masukkan Nilai2: "))
        hasil = modulus(value1, value2)
        print("The result of modulus", value1, "%", value2, "is",hasil)

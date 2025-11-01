a = int(input("Masukkan sisi A: "))
b = int(input("Masukkan sisi B: "))
c = int(input("Masukkan sisi C: "))
if ( (a + b <= c) or (a + c <= b) or (b + c <= a) ):
    print("Bukan Segitiga")
elif a == b == c:
    print("Segitiga Sama Sisi")
elif a == b or a == c or b == c:
    print("Segitiga Sama Kaki")
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Segitiga Siku-Siku")
else:
    print("Segitiga Sembarang")

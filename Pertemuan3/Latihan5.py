import math
a = float(input("Masukkan nilai A: "))
b = float(input("Masukkan nilai B: "))
c = float(input("Masukkan nilai C: "))

if a == 0:
    print("Ini bukan persamaan kuadrat")
else:
    D = b**2 - 4*a*c
    print(f"Persamaan kuadrat: {a}x^2 + {b}x + {c} = 0")
    print(f"Nilai diskriminan: {D}")

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Ini memiliki akar yang berbeda")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
elif D == 0:
    x = -b / (2*a)
    print("Ini memiliki akar ganda")
    print(f"x = {x}")
else:
    x1 = f"(-{b}/(2*{a})) + sqrt({-D})/(2*{a})i"
    x2 = f"(-{b}/(2*{a})) - sqrt({-D})/(2*{a})i"
    print("Ini memiliki akar imajiner")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

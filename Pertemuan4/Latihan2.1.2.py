max = int(input("Masukkan Nilai Max:"))
temp = ""

for i in range(max, 0, -1):
    for j in range (0, i, 1):
        temp = temp + str(i)
    temp = temp + "\n"

for i in range(2,max + 1, 1):
    for j in range (0,i, 1):
        temp = temp + str(i) 
    temp = temp + "\n"
print(temp)

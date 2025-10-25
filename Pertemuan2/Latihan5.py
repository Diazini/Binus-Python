import math

def haversine(lon1, lat1, lon2, lat2):
    """
    Menghitung jarak antara dua titik di permukaan bumi menggunakan rumus Haversine.
    Input dalam derajat.
    Output dalam kilometer.
    """

    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

 
    dlon = lon2 - lon1
    dlat = lat2 - lat1


    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))

 
    R = 6371.0


    distance = R * c
    return distance


print("=== Program Menghitung Jarak antara Dua Titik di Permukaan Bumi ===")
lon1 = float(input("Masukkan Longitude Titik A: "))
lat1 = float(input("Masukkan Latitude Titik A: "))
lon2 = float(input("Masukkan Longitude Titik B: "))
lat2 = float(input("Masukkan Latitude Titik B: "))

jarak = haversine(lon1, lat1, lon2, lat2)

print(f"\nJarak antara Titik A dan Titik B adalah: {jarak:.2f} km")


import math
radius_lingkaran = float(input("Masukkan radius lingkaran: "))


def luas_segitiga(r):
    alas = r*2
    tinggi = r
    luas = alas*tinggi/2
    return luas


luas_ungu = round(luas_segitiga(radius_lingkaran), 2)


def luas_lingkaran(r):
    luas = math.pi * (r**2)
    return luas


luas_kuning = round(luas_lingkaran(radius_lingkaran) - luas_ungu, 2)


def luas_persegi(r):
    sisi = r*2
    luas = sisi*sisi
    return luas


luas_merah = round(luas_persegi(radius_lingkaran) - (luas_kuning+luas_ungu), 2)


luas_merah = "%.2f" % luas_merah
luas_kuning = "%.2f" % luas_kuning
luas_ungu = "%.2f" % luas_ungu

print(f"Luas daerah cat merah: {luas_merah}")
print(f"Luas daerah cat kuning: {luas_kuning}")
print(f"Luas daerah cat ungu: {luas_ungu}")

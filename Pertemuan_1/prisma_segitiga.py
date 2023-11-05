# Menghitung volume prisma segitiga
def volume_prisma_segitiga(alas, tinggi_segitiga, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga
    volume = luas_alas * tinggi_prisma
    return volume

# Contoh penggunaan fungsi
alas_segitiga = float(input("Masukkan Alas Segitiga: "))  # Panjang alas segitiga
tinggi_segitiga = float(input("Masukkan Tinggi Segitiga: "))  # Tinggi segitiga
tinggi_prisma = float(input("Masukkan Tinggi Prisma Segitiga: "))  # Tinggi prisma

hasil_volume = volume_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma)
print("Volume prisma segitiga adalah:", hasil_volume)

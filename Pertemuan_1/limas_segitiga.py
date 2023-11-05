# Menghitung volume limas segitiga
panjang_alas = float(input("Masukkan Panjang alas: "))  # Panjang sisi alas segitiga
tinggi_limas = float(input("Masukkan Tinggi Limas: "))  # Tinggi limas
volume = (panjang_alas ** 2) * tinggi_limas / 6
print("Volume limas segitiga adalah:", volume)

# Menghitung luas permukaan limas segitiga
luas_permukaan = (panjang_alas ** 2) + (panjang_alas * (panjang_alas * (2 ** 0.5) / 2) * 3)
print("Luas permukaan limas segitiga adalah:", luas_permukaan)

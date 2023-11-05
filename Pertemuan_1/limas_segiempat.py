# Menghitung volume limas segiempat
panjang_alas = float(input("Masukkan Panjang Alas: "))  # Panjang sisi alas
tinggi_limas = float(input("Masukkan Tinggi Alas: "))  # Tinggi limas
volume = (panjang_alas ** 2) * tinggi_limas / 3
print("Volume limas segiempat adalah:", volume)

# Menghitung luas permukaan limas segiempat
luas_permukaan = (panjang_alas ** 2) + 4 * ((panjang_alas * tinggi_limas) / 2)
print("Luas permukaan limas segiempat adalah:", luas_permukaan)

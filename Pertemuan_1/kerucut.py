# Menghitung volume kerucut
jari_jari = float(input("Masukkan Jari-Jari: "))  # Jari-jari kerucut
tinggi = float(input("Masukkan Tinggi: "))  # Tinggi kerucut
volume = (1/3) * 3.14 * (jari_jari ** 2) * tinggi
print("Volume kerucut adalah:", volume)

# Menghitung luas permukaan kerucut
luas_permukaan = 3.14 * jari_jari * (jari_jari + ((jari_jari**2 + tinggi**2)**0.5))
print("Luas permukaan kerucut adalah:", luas_permukaan)

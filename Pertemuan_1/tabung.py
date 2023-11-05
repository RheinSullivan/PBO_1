# Menghitung volume tabung
jari_jari = float(input("Masukkan Jari-Jari: "))  # Jari-jari tabung
tinggi = float(input("Masukkan Tinggi: "))  # Tinggi tabung
volume = 3.14 * (jari_jari ** 2) * tinggi
print("Volume tabung adalah:", volume)

# Menghitung luas permukaan tabung
luas_permukaan = 2 * 3.14 * jari_jari * (jari_jari + tinggi)
print("Luas permukaan tabung adalah:", luas_permukaan)

import math

def hitung_luas_permukaan_tabung(jari_jari, tinggi):
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    return luas_permukaan

def hitung_volume_tabung(jari_jari, tinggi):
    volume = math.pi * jari_jari**2 * tinggi
    return volume

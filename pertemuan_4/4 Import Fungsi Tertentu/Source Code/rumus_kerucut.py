import math

def hitung_luas_permukaan_kerucut(jari_jari, tinggi):
    luas_permukaan = math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari**2 + tinggi**2))
    return luas_permukaan

def hitung_volume_kerucut(jari_jari, tinggi):
    volume = (1/3) * math.pi * jari_jari**2 * tinggi
    return volume

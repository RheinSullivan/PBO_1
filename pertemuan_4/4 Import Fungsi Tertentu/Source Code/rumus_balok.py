# rumus_balok.py

def hitung_luas_permukaan(panjang, lebar, tinggi):
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    return luas_permukaan

def hitung_volume(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume
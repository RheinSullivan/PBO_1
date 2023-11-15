import math

def hitung_luas_permukaan_limas_segitiga(alas_segitiga, tinggi_segitiga, tinggi_limas):
    luas_permukaan = alas_segitiga * tinggi_segitiga + 3 * (0.5 * alas_segitiga * math.sqrt(tinggi_segitiga**2 + (alas_segitiga/2)**2))
    return luas_permukaan

def hitung_volume_limas_segitiga(alas_segitiga, tinggi_segitiga, tinggi_limas):
    volume = (1/3) * (0.5 * alas_segitiga * tinggi_segitiga) * tinggi_limas
    return volume

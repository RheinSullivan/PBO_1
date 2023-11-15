def hitung_luas_permukaan_limas_segiempat(alas_segiempat, tinggi_segitiga, tinggi_limas):
    luas_permukaan = alas_segiempat**2 + 2 * alas_segiempat * (alas_segiempat / (2 * tinggi_segitiga)) * tinggi_limas
    return luas_permukaan

def hitung_volume_limas_segiempat(alas_segiempat, tinggi_segitiga, tinggi_limas):
    volume = (1/3) * (alas_segiempat**2) * tinggi_limas
    return volume

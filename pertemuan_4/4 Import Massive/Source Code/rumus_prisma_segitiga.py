def hitung_luas_permukaan_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma):
    luas_permukaan = 2 * (alas_segitiga * tinggi_segitiga + 3 * (0.5 * alas_segitiga * tinggi_prisma))
    return luas_permukaan

def hitung_volume_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma):
    volume = (alas_segitiga * tinggi_segitiga) * tinggi_prisma
    return volume

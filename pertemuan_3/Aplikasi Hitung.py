import tkinter as tk
from math import pi, sqrt

def hitung_luas_dan_volume():
    bentuk_bangun = combo_bangun.get()
    
    if bentuk_bangun == "Kubus":
        sisi = float(entry_sisi.get())
        luas = 6 * (sisi ** 2)
        volume = sisi ** 3
    elif bentuk_bangun == "Prisma Segitiga":
        alas = float(entry_alas.get())
        tinggi = float(entry_tinggi.get())
        sisi = float(entry_sisi.get())
        luas = 2 * (alas * tinggi + 0.5 * sisi * tinggi) + 3 * (sisi ** 2)
        volume = sisi * alas * tinggi
    elif bentuk_bangun == "Balok":
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        tinggi = float(entry_tinggi.get())
        sisi = float(entry_sisi.get())
        luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        volume = panjang * lebar * tinggi
    elif bentuk_bangun == "Limas Segiempat":
        alas_limas = float(entry_alas_limas.get())
        tinggi_limas = float(entry_tinggi_limas.get())
        sisi = float(entry_sisi.get())
        luas = alas_limas + 4 * (0.5 * sisi * tinggi_limas)
        volume = (0.5 * sisi * tinggi_limas * alas_limas) / 3
    elif bentuk_bangun == "Tabung":
        jari_tabung = float(entry_jari_tabung.get())
        tinggi_tabung = float(entry_tinggi_tabung.get())
        luas = 2 * pi * jari_tabung * (jari_tabung + tinggi_tabung)
        volume = pi * (jari_tabung ** 2) * tinggi_tabung
    elif bentuk_bangun == "Kerucut":
        jari_kerucut = float(entry_jari_kerucut.get())
        tinggi_kerucut = float(entry_tinggi_kerucut.get())
        luas = pi * jari_kerucut * (jari_kerucut + sqrt(jari_kerucut**2 + tinggi_kerucut**2))
        volume = (pi * (jari_kerucut ** 2) * tinggi_kerucut) / 3
    elif bentuk_bangun == "Bola":
        jari_bola = float(entry_jari_bola.get())
        luas = 4 * pi * (jari_bola ** 2)
        volume = (4/3) * pi * (jari_bola ** 3)
    else:
        luas = volume = 0

    hasil_luas_entry = f"Luas {bentuk_bangun}: {luas}"
    hasil_volume_entry = f"Volume {bentuk_bangun}: {volume}"
    entry_hasil_luas.insert(tk.END, hasil_luas_entry)
    entry_hasil_luas.config(state="readonly")

    entry_hasil_volume.insert(tk.END, hasil_volume_entry)
    entry_hasil_volume.config(state="readonly")

# Membuat jendela aplikasi
app = tk.Tk()
app.title("Kalkulator Bangun Ruang")

# Dropdown untuk memilih bentuk bangun ruang
label_bangun = tk.Label(app, text="Pilih Bentuk Bangun Ruang:")
label_bangun.pack()
bangun_ruang_options = ["Kubus", "Prisma Segitiga", "Balok", "Limas Segiempat", "Tabung", "Kerucut", "Bola"]
combo_bangun = tk.StringVar(app)
combo_bangun.set(bangun_ruang_options[0])  # Default pilihan
dropdown_bangun = tk.OptionMenu(app, combo_bangun, *bangun_ruang_options)
dropdown_bangun.pack()

# Label dan input untuk panjang sisi (umum)
label_sisi = tk.Label(app, text="Panjang Sisi:")
label_sisi.pack()

entry_sisi = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)
entry_sisi.pack()



# Label dan input tambahan untuk bentuk bangun ruang tertentu
label_alas = tk.Label(app, text="Alas (Hanya untuk Prisma Segitiga):")
entry_alas = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_panjang = tk.Label(app, text="Panjang (Hanya untuk Balok):")
entry_panjang = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_lebar = tk.Label(app, text="Lebar (Hanya untuk Balok):")
entry_lebar = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_tinggi = tk.Label(app, text="Tinggi:")
entry_tinggi = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_alas_limas = tk.Label(app, text="Alas Limas (Hanya untuk Limas Segiempat):")
entry_alas_limas = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_tinggi_limas = tk.Label(app, text="Tinggi Limas (Hanya untuk Limas Segiempat):")
entry_tinggi_limas = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_jari_tabung = tk.Label(app, text="Jari-jari Tabung (Hanya untuk Tabung):")
entry_jari_tabung = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_tinggi_tabung = tk.Label(app, text="Tinggi Tabung (Hanya untuk Tabung):")
entry_tinggi_tabung = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_jari_kerucut = tk.Label(app, text="Jari-jari Kerucut (Hanya untuk Kerucut):")
entry_jari_kerucut = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_tinggi_kerucut = tk.Label(app,text="Tinggi Kerucut (Hanya untuk Kerucut):")
entry_tinggi_kerucut = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_jari_bola = tk.Label(app, text="Jari-jari Bola (Hanya untuk Bola):")
entry_jari_bola = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

# Menentukan posisi widget entry
label_tinggi.pack()
entry_tinggi.pack()

label_panjang.pack()
entry_panjang.pack()

label_alas.pack()
entry_alas.pack()



label_lebar.pack()
entry_lebar.pack()

label_alas_limas.pack()
entry_alas_limas.pack()

label_tinggi_limas.pack()
entry_tinggi_limas.pack()

label_jari_tabung.pack()
entry_jari_tabung.pack()

label_tinggi_tabung.pack()
entry_tinggi_tabung.pack()

label_jari_kerucut.pack()
entry_jari_kerucut.pack()

label_tinggi_kerucut.pack()
entry_tinggi_kerucut.pack()

label_jari_bola.pack()
entry_jari_bola.pack()

# Tombol untuk menghitung luas dan volume
button_hitung = tk.Button(app, text="Hitung Luas & Volume", command=hitung_luas_dan_volume)
button_hitung.pack()

# Widget Text untuk menampilkan hasil
entry_hasil_luas = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30)
entry_hasil_luas.pack()

entry_hasil_volume = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30)
entry_hasil_volume.pack()



# Menjalankan aplikasi
app.mainloop()

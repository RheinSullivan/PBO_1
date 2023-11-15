import tkinter as tk
from rumus_limas_segiempat import *

def hitung_dan_tampilkan():
    alas_segiempat = float(alas_segiempat_entry.get())
    tinggi_segitiga = float(tinggi_segitiga_entry.get())
    tinggi_limas = float(tinggi_limas_entry.get())

    luas_permukaan = hitung_luas_permukaan_limas_segiempat(alas_segiempat, tinggi_segitiga, tinggi_limas)
    volume = hitung_volume_limas_segiempat(alas_segiempat, tinggi_segitiga, tinggi_limas)

    hasil_label.config(text=f"Luas Permukaan: {luas_permukaan}\nVolume: {volume}")

app = tk.Tk()
app.title("Kalkulator Limas Segiempat")

alas_segiempat_label = tk.Label(app, text="Alas Segiempat:")
alas_segiempat_label.pack()

alas_segiempat_entry = tk.Entry(app)
alas_segiempat_entry.pack()

tinggi_segitiga_label = tk.Label(app, text="Tinggi Segitiga:")
tinggi_segitiga_label.pack()

tinggi_segitiga_entry = tk.Entry(app)
tinggi_segitiga_entry.pack()

tinggi_limas_label = tk.Label(app, text="Tinggi Limas:")
tinggi_limas_label.pack()

tinggi_limas_entry = tk.Entry(app)
tinggi_limas_entry.pack()

hitung_button = tk.Button(app, text="Hitung", command=hitung_dan_tampilkan)
hitung_button.pack()

hasil_label = tk.Label(app, text="")
hasil_label.pack()

app.mainloop()

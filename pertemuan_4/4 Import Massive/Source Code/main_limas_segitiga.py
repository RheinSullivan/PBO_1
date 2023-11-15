import tkinter as tk
from rumus_limas_segitiga import *

def hitung_dan_tampilkan():
    alas_segitiga = float(alas_entry.get())
    tinggi_segitiga = float(tinggi_entry.get())
    tinggi_limas = float(tinggi_limas_entry.get())

    luas_permukaan = hitung_luas_permukaan_limas_segitiga(alas_segitiga, tinggi_segitiga, tinggi_limas)
    volume = hitung_volume_limas_segitiga(alas_segitiga, tinggi_segitiga, tinggi_limas)

    hasil_label.config(text=f"Luas Permukaan: {luas_permukaan}\nVolume: {volume}")

app = tk.Tk()
app.title("Kalkulator Limas Segitiga")

alas_label = tk.Label(app, text="Alas Segitiga:")
alas_label.pack()

alas_entry = tk.Entry(app)
alas_entry.pack()

tinggi_label = tk.Label(app, text="Tinggi Segitiga:")
tinggi_label.pack()

tinggi_entry = tk.Entry(app)
tinggi_entry.pack()

tinggi_limas_label = tk.Label(app, text="Tinggi Limas:")
tinggi_limas_label.pack()

tinggi_limas_entry = tk.Entry(app)
tinggi_limas_entry.pack()

hitung_button = tk.Button(app, text="Hitung", command=hitung_dan_tampilkan)
hitung_button.pack()

hasil_label = tk.Label(app, text="")
hasil_label.pack()

app.mainloop()

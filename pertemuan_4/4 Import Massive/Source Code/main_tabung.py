import tkinter as tk
from rumus_tabung import *

def hitung_dan_tampilkan():
    jari_jari = float(jari_jari_entry.get())
    tinggi = float(tinggi_entry.get())

    luas_permukaan = hitung_luas_permukaan_tabung(jari_jari, tinggi)
    volume = hitung_volume_tabung(jari_jari, tinggi)

    hasil_label.config(text=f"Luas Permukaan: {luas_permukaan}\nVolume: {volume}")

app = tk.Tk()
app.title("Kalkulator Tabung")

jari_jari_label = tk.Label(app, text="Jari-jari:")
jari_jari_label.pack()

jari_jari_entry = tk.Entry(app)
jari_jari_entry.pack()

tinggi_label = tk.Label(app, text="Tinggi:")
tinggi_label.pack()

tinggi_entry = tk.Entry(app)
tinggi_entry.pack()

hitung_button = tk.Button(app, text="Hitung", command=hitung_dan_tampilkan)
hitung_button.pack()

hasil_label = tk.Label(app, text="")
hasil_label.pack()

app.mainloop()

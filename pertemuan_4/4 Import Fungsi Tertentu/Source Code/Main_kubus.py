import tkinter as tk
from rumus_kubus import hitung_luas_permukaan_kubus, hitung_volume_kubus

def hitung_dan_tampilkan():
    sisi = float(sisi_entry.get())

    luas_permukaan = hitung_luas_permukaan_kubus(sisi)
    volume = hitung_volume_kubus(sisi)

    hasil_label.config(text=f"Luas Permukaan: {luas_permukaan}\nVolume: {volume}")

app = tk.Tk()
app.title("Kalkulator Kubus")

sisi_label = tk.Label(app, text="Panjang Sisi:")
sisi_label.pack()

sisi_entry = tk.Entry(app)
sisi_entry.pack()

hitung_button = tk.Button(app, text="Hitung", command=hitung_dan_tampilkan)
hitung_button.pack()

hasil_label = tk.Label(app, text="")
hasil_label.pack()

app.mainloop()

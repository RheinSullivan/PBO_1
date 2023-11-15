import tkinter as tk
from rumus_balok import hitung_luas_permukaan, hitung_volume

def hitung_dan_tampilkan():
    panjang = float(panjang_entry.get())
    lebar = float(lebar_entry.get())
    tinggi = float(tinggi_entry.get())

    luas_permukaan = hitung_luas_permukaan(panjang, lebar, tinggi)
    volume = hitung_volume(panjang, lebar, tinggi)

    hasil_label.config(text=f"Luas Permukaan: {luas_permukaan}\nVolume: {volume}")

app = tk.Tk()
app.title("Kalkulator Balok")

panjang_label = tk.Label(app, text="Panjang:")
panjang_label.pack()

panjang_entry = tk.Entry(app)
panjang_entry.pack()

lebar_label = tk.Label(app, text="Lebar:")
lebar_label.pack()

lebar_entry = tk.Entry(app)
lebar_entry.pack()

tinggi_label = tk.Label(app, text="Tinggi:")
tinggi_label.pack()

tinggi_entry = tk.Entry(app)
tinggi_entry.pack()

hitung_button = tk.Button(app, text="Hitung", command=hitung_dan_tampilkan)
hitung_button.pack()

hasil_label = tk.Label(app, text="")
hasil_label.pack()

app.mainloop()

import tkinter as tk
from rumus_bola import hitung_luas_permukaan_bola, hitung_volume_bola

def hitung_dan_tampilkan():
    jari_jari = float(jari_jari_entry.get())

    luas_permukaan = hitung_luas_permukaan_bola(jari_jari)
    volume = hitung_volume_bola(jari_jari)

    hasil_label.config(text=f"Luas Permukaan: {luas_permukaan}\nVolume: {volume}")

app = tk.Tk()
app.title("Kalkulator Bola")

jari_jari_label = tk.Label(app, text="Jari-jari:")
jari_jari_label.pack()

jari_jari_entry = tk.Entry(app)
jari_jari_entry.pack()

hitung_button = tk.Button(app, text="Hitung", command=hitung_dan_tampilkan)
hitung_button.pack()

hasil_label = tk.Label(app, text="")
hasil_label.pack()

app.mainloop()

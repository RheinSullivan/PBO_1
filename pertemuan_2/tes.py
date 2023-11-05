import tkinter as tk

def hitung_luas_dan_volume():
    entry_luas.delete(0, tk.END)  # Menghapus teks di entry_luas
    entry_volume.delete(0, tk.END)  # Menghapus teks di entry_volume

    sisi = float(entry_sisi.get())
    luas = 6 * (sisi ** 2)
    volume = sisi ** 3

    entry_luas.insert(0, f"Luas Kubus: {luas} satuan luas")
    entry_luas.config(state="readonly")

    entry_volume.insert(0, f"Volume Kubus: {volume} satuan volume")
    entry_volume.config(state="readonly")

def reset():
    entry_sisi.delete(0, tk.END)  # Menghapus teks di entry_sisi
    entry_luas.delete(0, tk.END)  # Menghapus teks di entry_luas
    entry_volume.delete(0, tk.END)  # Menghapus teks di entry_volume

app = tk.Tk()
app.title("Kalkulator Kubus")

label_sisi = tk.Label(app, text="Panjang Sisi:")
label_sisi.pack()

entry_sisi = tk.Entry(app)
entry_sisi.pack()

button_hitung = tk.Button(app, text="Hitung Luas & Volume", command=hitung_luas_dan_volume)
button_hitung.pack()

button_reset = tk.Button(app, text="Reset", command=reset)
button_reset.pack()

entry_luas = tk.Entry(app, width=40)
entry_luas.pack()

entry_volume = tk.Entry(app, width=40)
entry_volume.pack()

app.mainloop()

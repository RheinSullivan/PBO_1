import tkinter as tk
from tkinter import Frame, Label, Entry, Button, ttk, VERTICAL, YES, BOTH, END, StringVar, messagebox
from matakuliah import matakuliah


class FormMatakuliah:

    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # Label
        Label(mainFrame, text='Kode Mata Kuliah :').grid(
            row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtkodemk = Entry(mainFrame)
        self.txtkodemk.grid(row=0, column=1, padx=5, pady=5)
        # menambahkan event Enter key
        self.txtkodemk.bind("<Return>", self.onCari)

        Label(mainFrame, text='Nama Mata Kuliah :').grid(
            row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtnamamk = Entry(mainFrame)
        self.txtnamamk.grid(row=1, column=1, padx=5, pady=5)

        Label(mainFrame, text='Jumlah SKS :').grid(
            row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtsks = StringVar()
        Cbo = ttk.Combobox(mainFrame, width=27, textvariable=self.txtsks)
        Cbo.grid(row=3, column=1, padx=5, pady=5)
        Cbo['values'] = ('1', '2', '3', '4')
        Cbo.current()

        # Button
        self.btnSimpan = Button(mainFrame, text='Save',
                                command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear',
                               command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Clear', command=lambda: self.onDelete(
            self.txtkodemk.get()), width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('idmk', 'kodemk', 'namamk', 'sks')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idmk', text='ID')
        self.tree.column('idmk', width="30")
        self.tree.heading('kodemk', text='Kode Matakuliah')
        self.tree.column('kodemk', width="60")
        self.tree.heading('namamk', text='Nama Matakuliah')
        self.tree.column('namamk', width="200")
        self.tree.heading('sks', text='Jumlah sks')
        self.tree.column('sks', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()

    def onClear(self, event=None):
        self.txtkodemk.delete(0, END)
        self.txtnamamk.delete(0, END)
        self.txtsks.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False

    def onReload(self, event=None):
        # get data matakuliah
        mk = matakuliah()
        result = mk.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students = []
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('', END, values=student)

    def onCari(self, event=None):
        kodemk = self.txtkodemk.get()
        mk = matakuliah()
        res = mk.getBykodemk(kodemk)
        rec = mk.affected
        if (rec > 0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtnamamk.focus()
        return res

    def TampilkanData(self, event=None):
        kodemk = self.txtkodemk.get()
        mk = matakuliah()
        res = mk.getBykodemk(kodemk)
        self.txtnamamk.delete(0, END)
        self.txtnamamk.insert(END, mk.namamk)
        self.txtsks.set(mk.sks)
        self.btnSimpan.config(text="Update")

    def onSimpan(self, event=None):
        kodemk = self.txtkodemk.get()
        namamk = self.txtnamamk.get()
        sks = self.txtsks.get()
        mk = matakuliah()
        mk.kodemk = kodemk
        mk.namamk = namamk
        mk.sks = sks
        if (self.ditemukan == True):
            res = mk.updateBykodemk(kodemk)
            ket = 'Diperbarui'
        else:
            res = mk.simpan()
            ket = 'Disimpan'

        rec = mk.affected
        if (rec > 0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kodemk = self.txtkodemk.get()
        mk = matakuliah()
        res = mk.getBykodemk(kodemk)
        rec = mk.affected

        if rec > 0:
            # Jika data ditemukan, munculkan konfirmasi untuk menghapus
            confirm = messagebox.askyesno(
                "Konfirmasi", "Apakah Anda yakin ingin menghapus data?")
            if confirm:
                res = mk.deleteBykodemk(kodemk)
                rec = mk.affected
                if rec > 0:
                    messagebox.showinfo("showinfo", "Data Berhasil dihapus")
                else:
                    messagebox.showwarning(
                        "showwarning", "Gagal menghapus data")
        else:
            # Jika data tidak ditemukan, tampilkan pesan peringatan
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan")

        self.onClear()

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormMatakuliah(
        root, "Aplikasi Data Matakuliah")
    root.mainloop()

A = FormMatakuliah()
B = A.info
print(B)

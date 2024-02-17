# filename : FrmAnggota.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Anggota import Anggota
from db import DBConnection as mydb





class FrmAnggotaView:   
    def __init__(self, parent, title, update_main_window):
        self.parent = parent       
        self.update_main_window = update_main_window
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # define columns
        columns = ('Id','Nim','Nama','UKM','Angkatan','Jabatan','Kegiatan')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('Id', text='Id')
        self.tree.column('Id', width="30")
        self.tree.heading('Nim', text='Nim')
        self.tree.column('Nim', width="30")
        self.tree.heading('Nama', text='Nama')
        self.tree.column('Nama', width="100")
        self.tree.heading('UKM', text='UKM')
        self.tree.column('UKM', width="100")
        self.tree.heading('Angkatan', text='Angkatan')
        self.tree.column('Angkatan', width="100")
        self.tree.heading('Jabatan', text='Jabatan')
        self.tree.column('Jabatan', width="100")
        self.tree.heading('Kegiatan', text='Kegiatan')
        self.tree.column('Kegiatan', width="100")
        # set tree position
        self.tree.place(x=0, y=0)
        self.onReload()

    
    def onClear(self, event=None):

        self.txtNIM.delete(0,END)
        self.txtNIM.insert(END,"")
                                
        self.txtNAMA.delete(0,END)
        self.txtNAMA.insert(END,"")
                                
        self.txtUKM.set("")
            
        self.txtANGKATAN.delete(0,END)
        self.txtANGKATAN.insert(END,"")
                                
        self.txtJABATAN.delete(0,END)
        self.txtJABATAN.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False

        


    def onReload(self, event=None):
        # get data anggota
        obj = Anggota()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)

        for row in mylist:
            self.tree.insert('',END, values=row)
            


    def onCari(self, event=None):
        Nim = self.txtNIM.get()
        obj = Anggota()
        res = obj.getByNIM(Nim)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            


    def TampilkanData(self, event=None):
        Nim = self.txtNIM.get()
        obj = Anggota()
        res = obj.getByNIM(Nim)
            

        self.txtNAMA.delete(0,END)
        self.txtNAMA.insert(END,obj.Nama)
                                
        self.txtUKM.set(obj.UKM)
            
        self.txtANGKATAN.delete(0,END)
        self.txtANGKATAN.insert(END,obj.Angkatan)
                                
        self.txtJABATAN.delete(0,END)
        self.txtJABATAN.insert(END,obj.Jabatan)
                                

        self.btnSimpan.config(text="Update")



    def onSimpan(self, event=None):

        Nim = self.txtNIM.get()
        Nama = self.txtNAMA.get()
        UKM = self.txtUKM.get()
        Angkatan = self.txtANGKATAN.get()
        Jabatan = self.txtJABATAN.get()
        Kegiatan = self.txtKEGIATAN.get()       
        obj = Anggota()

        obj.Nim = Nim
        obj.Nama = Nama
        obj.UKM = UKM
        obj.Angkatan = Angkatan
        obj.Jabatan = Jabatan
        obj.Kegiatan = Kegiatan

        if(self.ditemukan==True):
            res = obj.updateByNIM(Nim)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec


    
    def onDelete(self, event=None):
        Nim = self.txtNIM.get()
        obj = Anggota()
        obj.Nim = Nim
        if(self.ditemukan==True):
            res = obj.deleteByNIM(Nim)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()


if __name__ == '__main__':
    def update_main_window(result):
        print(result)

    root = tk.Tk()
    aplikasi = FrmAnggotaView(root, "Aplikasi Data Anggota")
    root.mainloop() 
        
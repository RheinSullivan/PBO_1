# filename : FrmAnggota.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Anggota import Anggota
from db import DBConnection as mydb





class FormAnggota:   
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
        
        
            # int 

        Label(mainFrame, text='Nim :').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NIM
        self.txtNIM = Entry(mainFrame) 
        self.txtNIM.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNIM.bind("<Return>",self.onCari) # menambahkan event Enter key
                
            # varchar 

        Label(mainFrame, text='Nama :').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA
        self.txtNAMA = Entry(mainFrame) 
        self.txtNAMA.grid(row=1, column=1, padx=5, pady=5)
                
            # enum 

        Label(mainFrame, text='UKM :').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtUKM = StringVar()
        CboUKM = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtUKM) 
        CboUKM.grid(row=2, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboUKM['values'] = ('Himasantika','Himaster','HMTI','Computer Education')
        CboUKM.current()
        
        

            # varchar 

        Label(mainFrame, text='Angkatan :').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Textbox ANGKATAN
        self.txtANGKATAN = Entry(mainFrame) 
        self.txtANGKATAN.grid(row=3, column=1, padx=5, pady=5)
                
            # varchar 

        Label(mainFrame, text='Jabatan :').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Textbox JABATAN
        self.txtJABATAN = Entry(mainFrame) 
        self.txtJABATAN.grid(row=4, column=1, padx=5, pady=5)
                
            # text 

        Label(mainFrame, text='Kegiatan :').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtKEGIATAN = StringVar()
        CboKEGIATAN = ttk.Combobox(mainFrame, width = 17, height=20, textvariable = self.txtKEGIATAN) 
        CboKEGIATAN.grid(row=5, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        # CboKEGIATAN['values'] = ('kegiatan UKM')
        # CboKEGIATAN.current()
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Save', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Delete', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        def updateUkmKegiatan():
            ukm_terpilih = self.txtUKM.get()
            if ukm_terpilih in ['Himasantika']:
                # self.txtKEGIATAN.delete (0,END)
                # self.txtKEGIATAN.insert(0, "")
                db = mydb()
                ukms = db.findAll("SELECT Kegiatan FROM kegiatan WHERE UKM = 'Himasantika'")
                ukm_values = [ukm[0] for ukm in ukms]
                self.txtKEGIATAN.set(ukm_values[0])
                CboKEGIATAN['values'] = ukm_values
                CboKEGIATAN.current()
            elif ukm_terpilih in ['Himaster']:
                # self.txtKEGIATAN.delete (0,END)
                # self.txtKEGIATAN.insert(0, "")
                db = mydb()
                ukms = db.findAll("SELECT Kegiatan FROM kegiatan WHERE UKM = 'Himaster'")
                ukm_values = [ukm[0] for ukm in ukms]
                self.txtKEGIATAN.set(ukm_values[0])
                CboKEGIATAN['values'] = ukm_values
                CboKEGIATAN.current()
            elif ukm_terpilih in ['HMTI']:
                # self.txtKEGIATAN.delete (0,END)
                # self.txtKEGIATAN.insert(0, "")
                db = mydb()
                ukms = db.findAll("SELECT Kegiatan FROM kegiatan WHERE UKM = 'HMTI'")
                ukm_values = [ukm[0] for ukm in ukms]
                self.txtKEGIATAN.set(ukm_values[0])
                CboKEGIATAN['values'] = ukm_values
                CboKEGIATAN.current()
            elif ukm_terpilih in ['Computer Education']:
                # self.txtKEGIATAN.delete (0,END)
                # self.txtKEGIATAN.insert(0, "")
                db = mydb()
                ukms = db.findAll("SELECT Kegiatan FROM kegiatan WHERE UKM = 'Computer Education'")
                ukm_values = [ukm[0] for ukm in ukms]
                self.txtKEGIATAN.set(ukm_values[0])
                CboKEGIATAN['values'] = ukm_values
                CboKEGIATAN.current()
            elif ukm_terpilih in ['Akatsuki']:
                # self.txtKEGIATAN.delete (0,END)
                # self.txtKEGIATAN.insert(0, "")
                db = mydb()
                ukms = db.findAll("SELECT Kegiatan FROM kegiatan WHERE UKM = 'Akatsuki'")
                ukm_values = [ukm[0] for ukm in ukms]
                self.txtKEGIATAN.set(ukm_values[0])
                CboKEGIATAN['values'] = ukm_values
                CboKEGIATAN.current()


        updateUkmKegiatan()  # Panggil fungsi pertama kali untuk menginisialisasi nilai film berdasarkan hari yang dipilih

        CboUKM.bind("<<ComboboxSelected>>", lambda event: updateUkmKegiatan())
        
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
        self.tree.place(x=0, y=250)
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
    aplikasi = FormAnggota(root, "Aplikasi Data Anggota")
    root.mainloop() 
        
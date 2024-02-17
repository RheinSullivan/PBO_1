# filename : FrmKegiatan.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Kegiatan import Kegiatan

from tkcalendar import Calendar, DateEntry

class FormKegiatan:   
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
        
        
            # varchar 

        Label(mainFrame, text='No :').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NO
        self.txtNO = Entry(mainFrame) 
        self.txtNO.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNO.bind("<Return>",self.onCari) # menambahkan event Enter key
                
            # varchar 

        Label(mainFrame, text='UKM :').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox UKM
        self.txtUKM = Entry(mainFrame) 
        self.txtUKM.grid(row=1, column=1, padx=5, pady=5)
                
            # text 

        Label(mainFrame, text='Kegiatan :').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtKEGIATAN = StringVar()
        CboKEGIATAN = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtKEGIATAN) 
        CboKEGIATAN.grid(row=2, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboKEGIATAN['values'] = ('Kegiatan UKM')
        CboKEGIATAN.current()
        
            # date 

        Label(mainFrame, text='Tanggal :').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Date Input TGL
        self.txtTGL = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTGL.grid(row=3, column=1, padx=5, pady=5)
                    
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('Id','No','UKM','Kegiatan','Tgl')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('Id', text='Id')
        self.tree.column('Id', width="30")
        self.tree.heading('No', text='No')
        self.tree.column('No', width="30")
        self.tree.heading('UKM', text='UKM')
        self.tree.column('UKM', width="100")
        self.tree.heading('Kegiatan', text='Kegiatan')
        self.tree.column('Kegiatan', width="100")
        self.tree.heading('Tgl', text='Tgl')
        self.tree.column('Tgl', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()

    
    def onClear(self, event=None):

        self.txtNO.delete(0,END)
        self.txtNO.insert(END,"")
                                
        self.txtUKM.delete(0,END)
        self.txtUKM.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False

        


    def onReload(self, event=None):
        # get data kegiatan
        obj = Kegiatan()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)

        for row in mylist:
            self.tree.insert('',END, values=row)
            


    def onCari(self, event=None):
        No = self.txtNO.get()
        obj = Kegiatan()
        res = obj.getByNO(No)
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
        No = self.txtNO.get()
        obj = Kegiatan()
        res = obj.getByNO(No)
            

        self.txtUKM.delete(0,END)
        self.txtUKM.insert(END,obj.UKM)
                                
        self.txtTGL.delete(0,END)
        self.txtTGL.insert(END,obj.Tgl)
                                

        self.btnSimpan.config(text="Update")



    def onSimpan(self, event=None):

        No = self.txtNO.get()
        UKM = self.txtUKM.get()
        Kegiatan = self.txtKEGIATAN.get()
        Tgl = self.txtTGL.get()       
        obj = Kegiatan()

        obj.No = No
        obj.UKM = UKM
        obj.Kegiatan = Kegiatan
        obj.Tgl = Tgl

        if(self.ditemukan==True):
            res = obj.updateByNO(No)
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
        No = self.txtNO.get()
        obj = Kegiatan()
        obj.No = No
        if(self.ditemukan==True):
            res = obj.deleteByNO(No)
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
    root = tk.Tk()
    aplikasi = FormKegiatan(root, "Aplikasi Data Kegiatan")
    root.mainloop()  
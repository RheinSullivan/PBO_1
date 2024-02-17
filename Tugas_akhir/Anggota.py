# filename : Anggota.py
from db import DBConnection as mydb

class Anggota:

    def __init__(self):
        self.__Id=None
        self.__Nim=None
        self.__Nama=None
        self.__UKM=None
        self.__Angkatan=None
        self.__Jabatan=None
        self.__Kegiatan=None

        self.conn = None
        self.affected = None
        self.result = None


    @property
    def Id(self):
        return self.__Id

    @property
    def Nim(self):
        return self.__Nim
        
    @Nim.setter
    def Nim(self, value):
        self.__Nim = value

    @property
    def Nama(self):
        return self.__Nama
        
    @Nama.setter
    def Nama(self, value):
        self.__Nama = value

    @property
    def UKM(self):
        return self.__UKM
        
    @UKM.setter
    def UKM(self, value):
        self.__UKM = value

    @property
    def Angkatan(self):
        return self.__Angkatan
        
    @Angkatan.setter
    def Angkatan(self, value):
        self.__Angkatan = value

    @property
    def Jabatan(self):
        return self.__Jabatan
        
    @Jabatan.setter
    def Jabatan(self, value):
        self.__Jabatan = value

    @property
    def Kegiatan(self):
        return self.__Kegiatan
        
    @Kegiatan.setter
    def Kegiatan(self, value):
        self.__Kegiatan = value





    def simpan(self):
        self.conn = mydb()
        val = (self.__Nim,self.__Nama,self.__UKM,self.__Angkatan,self.__Jabatan,self.__Kegiatan)
        sql="INSERT INTO Anggota (Nim,Nama,UKM,Angkatan,Jabatan,Kegiatan) VALUES " + str(val)

        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__Nim,self.__Nama,self.__UKM,self.__Angkatan,self.__Jabatan,self.__Kegiatan, id)
        sql="UPDATE anggota SET Nim = %s,Nama = %s,UKM = %s,Angkatan = %s,Jabatan = %s,Kegiatan = %s WHERE Id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIM(self, Nim):
        self.conn = mydb()
        val = (self.__Nama,self.__UKM,self.__Angkatan,self.__Jabatan,self.__Kegiatan, Nim)
        sql="UPDATE anggota SET Nama = %s,UKM = %s,Angkatan = %s,Jabatan = %s,Kegiatan = %s WHERE Nim=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM anggota WHERE Id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIM(self, Nim):
        self.conn = mydb()
        sql="DELETE FROM anggota WHERE Nim='" + str(Nim) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM anggota WHERE Id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)

        self.__Id = self.result[0]
        self.__Nim = self.result[1]
        self.__Nama = self.result[2]
        self.__UKM = self.result[3]
        self.__Angkatan = self.result[4]
        self.__Jabatan = self.result[5]
        self.__Kegiatan = self.result[6]
        self.conn.disconnect
        return self.result

    def getByNIM(self, Nim):
        a=str(Nim)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM anggota WHERE Nim='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__Id = self.result[0]
            self.__Nim = self.result[1]
            self.__Nama = self.result[2]
            self.__UKM = self.result[3]
            self.__Angkatan = self.result[4]
            self.__Jabatan = self.result[5]
            self.__Kegiatan = self.result[6]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__Id = ''
            self.__Nim = ''
            self.__Nama = ''
            self.__UKM = ''
            self.__Angkatan = ''
            self.__Jabatan = ''
            self.__Kegiatan = ''
        
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM anggota"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,Nama FROM anggota"
        self.result = self.conn.findAll(sql)
        return self.result        
            
from db import DBConnection as mydb

class Kegiatan:

    def __init__(self):
        self.__Id=None
        self.__No=None
        self.__UKM=None
        self.__Kegiatan=None
        self.__Tgl=None

        self.conn = None
        self.affected = None
        self.result = None


    @property
    def Id(self):
        return self.__Id

    @property
    def No(self):
        return self.__No
        
    @No.setter
    def No(self, value):
        self.__No = value

    @property
    def UKM(self):
        return self.__UKM
        
    @UKM.setter
    def UKM(self, value):
        self.__UKM = value

    @property
    def Kegiatan(self):
        return self.__Kegiatan
        
    @Kegiatan.setter
    def Kegiatan(self, value):
        self.__Kegiatan = value

    @property
    def Tgl(self):
        return self.__Tgl
        
    @Tgl.setter
    def Tgl(self, value):
        self.__Tgl = value





    def simpan(self):
        self.conn = mydb()
        val = (self.__No,self.__UKM,self.__Kegiatan,self.__Tgl)
        sql="INSERT INTO Kegiatan (No,UKM,Kegiatan,Tgl) VALUES " + str(val)

        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__No,self.__UKM,self.__Kegiatan,self.__Tgl, id)
        sql="UPDATE kegiatan SET No = %s,UKM = %s,Kegiatan = %s,Tgl = %s WHERE Id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNO(self, No):
        self.conn = mydb()
        val = (self.__UKM,self.__Kegiatan,self.__Tgl, No)
        sql="UPDATE kegiatan SET UKM = %s,Kegiatan = %s,Tgl = %s WHERE No=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM kegiatan WHERE Id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNO(self, No):
        self.conn = mydb()
        sql="DELETE FROM kegiatan WHERE No='" + str(No) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM kegiatan WHERE Id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)

        self.__Id = self.result[0]
        self.__No = self.result[1]
        self.__UKM = self.result[2]
        self.__Kegiatan = self.result[3]
        self.__Tgl = self.result[4]
        self.conn.disconnect
        return self.result

    def getByNO(self, No):
        a=str(No)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM kegiatan WHERE No='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__Id = self.result[0]
            self.__No = self.result[1]
            self.__UKM = self.result[2]
            self.__Kegiatan = self.result[3]
            self.__Tgl = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__Id = ''
            self.__No = ''
            self.__UKM = ''
            self.__Kegiatan = ''
            self.__Tgl = ''
        
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM kegiatan"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,UKM FROM kegiatan"
        self.result = self.conn.findAll(sql)
        return self.result         
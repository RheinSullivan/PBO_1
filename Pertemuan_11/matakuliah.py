from db import DBConnection


class matakuliah:

    def __init__(self):
        self.__id = None
        self.__kodemk = None
        self.__namamk = None
        self.__sks = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @property
    def kodemk(self):
        return self.__kodemk

    @kodemk.setter
    def kodemk(self, value):
        self.__kodemk = value

    @property
    def namamk(self):
        return self.__namamk

    @namamk.setter
    def namamk(self, value):
        self.__namamk = value

    @property
    def sks(self):
        return self.__sks

    @sks.setter
    def sks(self, value):
        self.__sks = value

    def simpan(self):
        self.conn = DBConnection()
        val = (self.__kodemk, self.__namamk, self.__sks)
        sql = "INSERT INTO matakuliah (kodemk, namamk, sks) VALUES (%s, %s, %s)"
        self.affected = self.conn.insert(sql, val)
        self.conn.disconnect()
        return self.affected

    def update(self, id):
        self.conn = DBConnection()
        val = (self.__kodemk, self.__namamk, self.__sks, id)
        sql = "UPDATE matakuliah SET kodemk = %s, namamk = %s, sks=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def updateBykodemk(self, kodemk):
        self.conn = DBConnection()
        val = (self.__namamk, self.__sks, kodemk)
        sql = "UPDATE matakuliah SET namamk = %s, sks=%s WHERE kodemk=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def delete(self, id):
        self.conn = DBConnection()
        sql = "DELETE FROM matakuliah WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect()
        return self.affected

    def deleteBykodemk(self, kodemk):
        self.conn = DBConnection()
        sql = "DELETE FROM matakuliah WHERE kodemk='" + str(kodemk) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect()
        return self.affected

    def getByID(self, id):
        self.conn = DBConnection()
        sql = "SELECT * FROM matakuliah WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kodemk = self.result[1]
        self.__namamk = self.result[2]
        self.__sks = self.result[3]
        self.conn.disconnect()
        return self.result

    def getBykodemk(self, kodemk):
        a = str(kodemk)
        b = a.strip()
        self.conn = DBConnection()
        sql = "SELECT * FROM matakuliah WHERE kodemk='" + b + "'"
        self.result = self.conn.findOne(sql)
        if self.result is not None:
            self.__kodemk = self.result[1]
            self.__namamk = self.result[2]
            self.__sks = self.result[3]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kodemk = ''
            self.__namamk = ''
            self.__sks = ''
            self.affected = 0
        self.conn.disconnect()
        return self.result

    def getAllData(self):
        self.conn = DBConnection()
        sql = "SELECT * FROM matakuliah"
        self.result = self.conn.findAll(sql)
        return self.result

import sqlite3
import initialDB

class SqlDatabase:
    Message = ""

    @staticmethod
    def Connect():
        try:
            connection = sqlite3.connect('CDMS-data.db')
            SqlDatabase.Message = "Connected"
            return connection
        except Exception as e:
            SqlDatabase.Message = e
        

    @staticmethod
    def Close(self, Connection):
        Connection.close()


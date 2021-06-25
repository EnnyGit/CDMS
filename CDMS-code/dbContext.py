import sqlite3
import initialDB

class SQLite:
    Message = ""

    @staticmethod
    def Connect():
        try:
            connection = sqlite3.connect('CDMS-data.db')
            SQLite.Message = "Connected"
            return connection
        except Exception as e:
            SQLite.Message = e

    @staticmethod
    def Close(self, Connection):
        Connection.close()

    #cursor = connection.cursor()
    #cursor.execute("INSERT INTO user VALUES ('Admin', 'Password123', 'Enny', 'Adeoye', '2021')")


    # This is the qmark style:
    #cursor.execute("create table lang (name, first_appeared)")
    #cursor.execute("INSERT INTO lang VALUES (?, ?)", ("C", 1972))

    #connection.commit()
    #connection.close()

SQLite.Connect()
print(SQLite.Message)
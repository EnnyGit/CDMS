import sqlite3
import initialDB

connection = sqlite3.connect('CDMS-data.db')
cursor = connection.cursor()

# This is the qmark style:
#cursor.execute("create table lang (name, first_appeared)")
#cursor.execute("INSERT INTO lang VALUES (?, ?)", ("C", 1972))

connection.commit()
connection.close()

import sqlite3

# Creates connection
connection = sqlite3.connect('example.db')

# Creates a Cursor object
cursor = connection.cursor()

# Execute SQL command
cursor.execute('''CREATE TABLE stocks (
    date text,
    trans text,
    symbol text,
    qty real,
    price real
)''')

# Insert a row of data
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
connection.commit()

# Close connection
connection.close()

# This is the qmark style:
cursor.execute("create table lang (name, first_appeared)")
cursor.execute("INSERT INTO lang VALUES (?, ?)", ("C", 1972))

# Datatypes
# NULL
# INTEGER
# REAL 
# TEXT
# BLOB
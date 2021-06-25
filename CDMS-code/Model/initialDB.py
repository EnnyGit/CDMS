import sqlite3

def CreateUserTable(cursor):
    return cursor.execute('''CREATE TABLE user (
        username text,
        password text,
        firstname text,
        lastname text,
        registrationdate text
    )''')

def CreateClientTable(cursor):
    return cursor.execute('''CREATE TABLE client (
        firstname text,
        lastname text,
        address text,
        lastname text,
        registrationdate text
    )''')
    
import sqlite3

def CreateUserTable():
    return ('''CREATE TABLE user (
        username text,
        password text,
        firstname text,
        lastname text,
        registrationdate text
    )''')

def CreateClientTable():
    return ('''CREATE TABLE 'client' (
        id INTEGER PRIMARY KEY,
        firstname TEXT,
        lastname TEXT,
        streetname TEXT,
        housenumber TEXT,
        zipcode TEXT,
        city TEXT,
        email TEXT,
        phone TEXT
    )''')
    
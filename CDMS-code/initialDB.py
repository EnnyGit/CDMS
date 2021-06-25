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
    return ('''CREATE TABLE client (
        firstname text,
        lastname text,
        address blob,
        email text,
        phone text
    )''')
    
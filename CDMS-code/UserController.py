from dbContext import SqlDatabase
from datetime import date, datetime
from UserModel import User
from random import randint
import Config
from ValidationController import Validation


class UserController:

    __db=None
    validator = Validation()

    def __init__(self):
        self.__db= SqlDatabase.Connect()

    def __sendToDatabase(self, user):
        try:
            cursor = self.__db.cursor()
            registrationdate = f'{date.today().strftime("%d-%m-%Y")}, {datetime.now().strftime("%H:%M:%S")}'
            query = f"INSERT INTO 'user' VALUES (NULL, '{user.GetUsername()}', '{user.GetPassword()}', '{user.GetFname()}', '{user.GetLname()}', '{registrationdate}', '{user.GetRole()}');"
            cursor.execute(query)
            self.__db.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False

    def Save(self, user, role):
        if self.__isAuthenticUsername(user):
            if self.__isValid(user):
                user.SetRole(role)
                if self.__sendToDatabase(user):
                    print(f"User {user.GetFname()} {user.GetLname()} was registered successfully")
            else:
                print("Please fill in all the fields!")
        else:
            print("Username already exists, please try a new one.")

    def UpdateUser(self, user):
        query = f"UPDATE 'user' SET firstname = '{user.GetFname()}', lastname = '{user.GetLname()}', username = '{user.GetUsername()}', password = '{user.GetPassword()}' WHERE id = '{user.GetId()}'"
        try:
            cursor = self.__db.cursor()
            cursor.execute(query)
            self.__db.commit()
            print("User information was changed successfully!")
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False

    def __isValid(self, user):
        if user.GetFname() !="" and user.GetLname() != "" and user.GetPassword() != "" and user.GetUsername() != "":
            return True
        return False

    def __isAuthenticUsername(self, user):
        cursor = self.__db.cursor()
        cursor.execute(f"SELECT id FROM 'user' WHERE username = '{user.GetUsername()}'")
        record = cursor.fetchone()
        if record == None:
            return True
        return False

    def GetUserByName(self, param, role):
        try:
            userList = []
            cursor = self.__db.cursor()
            query = f"SELECT * FROM 'user' WHERE firstname || ' ' || lastname LIKE '%{param}%' AND role = '{role}'"
            cursor.execute(query)
            dbData = cursor.fetchall()
            for user in dbData:
                userList.append(User(user[0], user[1], user[2], user[3], user[4], user[5], user[6]))
            return userList
        except Exception as e:
            print("Usercontroller Line 75: " , e)

    def GetUserByUsername(self, param, role):
        try:
            userList = []
            cursor = self.__db.cursor()
            query = f"SELECT * FROM 'user' WHERE username LIKE '%{param}%' AND role = '{role}'"
            cursor.execute(query)
            dbData = cursor.fetchall()
            for user in dbData:
                userList.append(User(user[0], user[1], user[2], user[3], user[4], user[5], user[6]))
            return userList
        except Exception as e:
            print("Usercontroller Line 88: " , e)

    def NewTempPassword(self):
        chars = '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/'''
        temppassword = f'{chars[randint(0,9)]}{chars[randint(0,9)]}{chars[randint(10,35)]}{chars[randint(10,35)]}{chars[randint(36,61)]}{chars[randint(36,61)]}{chars[randint(62,92)]}{chars[randint(62,92)]}'
        return temppassword
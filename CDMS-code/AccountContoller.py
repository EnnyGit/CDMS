from dbContext import SqlDatabase
from UserModel import User
import Config


class AccountController:

    __db=None

    def __init__(self):
        self.__db= SqlDatabase.Connect()

    def __sendToDatabase(self, user):
        try:
            cursor = self.__db.cursor()
            query = f"INSERT INTO 'user' VALUES (NULL, '{user.GetUsername()}', '{user.GetPassword()}', '{user.GetFname()}', '{user.GetLname()}', '{user.GetRegistrationDate()}', '{user.GetRole()}');"
            cursor.execute(query)
            self.__db.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False

    def Save(self, user):
        if self.__isValid(user):
            if self.__sendToDatabase(user):
                Config.loggedInUser = user
                print(f"User {user.GetUsername()} was registered successfully")
        else:
            print("Please fill in all  the fields!")
            

    def __isValid(self, user):
        if user.GetUsername() !="" and user.GetPassword() != "":
            return True
        return False
            
    def Login(self, user):
        if self.__isValid(user):
            if self.__isAuthentic(user):
                self.__authorize(user)
                self.SetLogedInUserData(user)
            else:
                print("Incorrect username or password")
        else:
            print("Please write a username and a password")

    def __isAuthentic(self, user):
        cursor = self.__db.cursor()
        cursor.execute("SELECT id FROM 'user' WHERE username = '"+user.GetUsername()+"' AND password = '"+user.GetPassword()+"'")
        record = cursor.fetchone()
        if record!=None:
            return True
        return False

    def __authorize(self, user):
        print(user.GetUsername() + " is Logged In...")

    def Remove(self, user):
        if self.__isValid(user):
            if self.__isAuthentic(user):
                if self.__DelUser(user):
                    print(f"User {user.GetUsername()}  was deleted successfully")
            else:
                print("User with these credentials does not exist!")
        else:
            print("Please write a username and a password")

    def __DelUser(self, user):
        try:
            cursor = self.__db.cursor()
            query = f"DELETE FROM 'user' WHERE username = '{user.GetUsername()}'"
            cursor.execute(query)
            self.__db.commit()
            return True
        except Exception as e:
            print(e)
            return False      
        finally:
            cursor.close()  

    def SetLogedInUserData(self, user):
        try:
            cursor = self.__db.cursor()
            query = f"SELECT * FROM 'user' WHERE username = '{user.GetUsername()}' AND password = '{user.GetPassword()}'"
            cursor.execute(query)
            dbData = cursor.fetchone()
            dbUser = User(dbData[0], dbData[1], dbData[2], dbData[3], dbData[4], dbData[5], dbData[6])
            Config.loggedInUser = dbUser
        except Exception as e:
            print(e)

    def ChangePassword(self, user):
        if self.IsValidLogin(user):
            if self.IsAuthentic(user):
                self.UpdatePassword(user)
            else:
                print("The username and password is Incorrect")
                return False
        else:
            print("Please write a username and a password")
            return False

    def UpdatePassword(self, user):
        
        user.SetPassword(input("Create a new Password: "))
        query = f"UPDATE 'user' SET password = '{user.GetPassword()}' WHERE username = '{user.GetUsername()}'"
        try:
            cursor = self.__db.cursor()
            cursor.execute(query)
            self.__db.commit()
            print("Password was changed successfully!")
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False
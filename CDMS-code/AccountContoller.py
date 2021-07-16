from dbContext import SqlDatabase
from UserModel import User
from LoggingController import LoggingController
from LogModel import Log
import Config


class AccountController:

    __db=None
    _logger = LoggingController()

    def __init__(self):
        self.__db= SqlDatabase.Connect()

    def __sendToDatabase(self, user):
        try:
            cursor = self.__db.cursor()
            query = f"INSERT INTO 'user' VALUES (NULL, '{user.GetUsername()}', '{user.GetPassword()}', '{user.GetFname()}', '{user.GetLname()}', '{user.GetRegistrationDate()}', '{user.GetRole()}');"
            cursor.execute(query)
            self.__db.commit()
            cursor.close()
            self._logger.Log(Log(
                suspicious="No",
                description=f"New {user.GetRole()} user is created",
                information=f"User name: {user.GetUsername()}"
            ))
            return True
        except Exception as e:
            print(e)
            return False

    def Save(self, user):
        if self.__isValid(user):
            if self.__sendToDatabase(user):
                print(f" INFO: User {user.GetUsername()} was registered successfully\n")
        else:
            print(" ERROR: Please fill in all  the fields!\n")
            

    def __isValid(self, user):
        if user.GetUsername() !="" and user.GetPassword() != "":
            return True
        return False
            
    def Login(self, user):
        if self.__isValid(user):
            if self.__isAuthentic(user):
                self._logger.Log(Log(
                    suspicious="No",
                    description="Logged In",
                    information=""
                ))
                self.SetLogedInUserData(user)
                return True
            else:
                self._logger.Log(Log(
                    suspicious="Yes",
                    description="Unsuccessful login",
                    information=f"Password '{user.GetPassword()}'' is tried in combination with Username '{user.GetUsername()}'"
                ))
                print(" ERROR: Incorrect username or password\n")
                return False
        else:
            print(" ERROR: Please write a username and a password\n")
            return False

    def __isAuthentic(self, user):
        cursor = self.__db.cursor()
        cursor.execute("SELECT id FROM 'user' WHERE username = '"+user.GetUsername()+"' AND password = '"+user.GetPassword()+"'")
        record = cursor.fetchone()
        Config.currentUsername = user.GetUsername()
        if record!=None:
            return True
        return False

    def Remove(self, user):
        if self.__isValid(user):
            if self.__isAuthentic(user):
                if self.__DelUser(user):
                    print(f" INFO: User {user.GetUsername()}  was deleted successfully\n")
                    self._logger.Log(Log(
                        suspicious="No",
                        description=f"{user.GetRole()} user is deleted",
                        information=f"User \"{user.GetUsername()}\" is deleted"
                    ))
            else:
                print(" INFO: User with these credentials does not exist!\n")
        else:
            print(" INFO: Please write a username and a password\n")

    def __DelUser(self, user):
        try:
            cursor = self.__db.cursor()
            query = f"DELETE FROM 'id' WHERE username = '{user.GetId()}'"
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
            Config.currentUsername = dbUser.GetUsername()
        except Exception as e:
            print(e)

    def ChangePassword(self, user):
        if self.IsValidLogin(user):
            if self.IsAuthentic(user):
                self.UpdatePassword(user)
                self._logger.Log(Log(
                    suspicious="No",
                    description=f"Update password",
                    information=f"Password of {user.GetUsername()} has been updated"
                ))
            else:
                print(" INFO: The username and password is Incorrect\n")
                return False
        else:
            print(" INFO: Please write a username and a password\n")
            return False

    def UpdatePassword(self, user):
        user.SetPassword(input("Create a new Password: "))
        query = f"UPDATE 'user' SET password = '{user.GetPassword()}' WHERE username = '{user.GetUsername()}'"
        try:
            cursor = self.__db.cursor()
            cursor.execute(query)
            self.__db.commit()
            print("INFO: Password was changed successfully!\n")
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False
from dbContext import SqlDatabase

class AccountController:

    __db=None
    __user=None
    loggedinuser = None

    def __init__(self):
        self.__db= SqlDatabase.Connect()

    def __sendToDatabase(self, user):
        try:
            cursor = self.__db.cursor()
            query = f"INSERT INTO 'user' VALUES (NULL, '{user.GetUsername()}', '{user.GetPassword()}');"
            cursor.execute(query)
            self.__db.commit()
            cursor.close()
            return True
        except Exception as e:
            user.SetMessage(e)
            return False

    def Save(self, user):
        if self.__isvalid(user):
            if self.__sendToDatabase(user):
                user.SetMessage(f"User {user.GetUsername()} was registered successfully")
        else:
            user.SetMessage("Please fill in all  the fields!")
            

    def __isvalid(self, user):
        if user.GetUsername() !="" and user.GetPassword() != "":
            return True
        return False
            
    def Login(self, user):
        if self.IsValidLogin(user):
            if self.IsAuthentic(user):
                self.Authorize(user)
                self.user=user
                AccountController.loggedinuser = user
                #TODO Check user access level
                AccountController.loggedinuser.role = 'admin'
            else:
                user.SetMessage("Incorrect username or password")
        else:
            user.SetMessage("Please write a username and a password")

    def IsValidLogin(self, user):
        if user.GetUsername() != "" and user.GetPassword != "":
            return True
        return False

    def IsAuthentic(self, user):
        cursor = self.__db.cursor()
        cursor.execute("SELECT id FROM 'user' WHERE username = '"+user.GetUsername()+"' AND password = '"+user.GetPassword()+"'")
        record = cursor.fetchone()
        if record!=None:
            return True
        return False

    def Authorize(self, user):
        user.SetMessage(user.GetUsername() + " is Logged In...")

    def Remove(self, user):
        if self.__isvalid(user):
            if self.IsAuthentic(user):
                if self.__DelUser(user):
                    user.SetMessage(f"User {user.GetUsername()}  was deleted successfully")
            else:
                user.SetMessage("User with these credentials does not exist!")
        else:
            user.SetMessage("Please write a username and a password")

    def __DelUser(self, user):
        try:
            cursor = self.__db.cursor()
            query = f"DELETE FROM 'user' WHERE username = '{user.GetUsername()}'"
            cursor.execute(query)
            self.__db.commit()
            return True
        except Exception as e:
            user.SetMessage(e)
            return False      
        finally:
            cursor.close()  

    def ChangePassword(self, user):
        if self.IsValidLogin(user):
            if self.IsAuthentic(user):
                self.UpdatePassword(user)
            else:
                user.SetMessage("The username and password is Incorrect")
                return False
        else:
            user.SetMessage("Please write a username and a password")
            return False

    def UpdatePassword(self, user):
        
        user.SetPassword(input("Create a new Password: "))
        query = f"UPDATE 'user' SET password = '{user.GetPassword()}' WHERE username = '{user.GetUsername()}'"
        try:
            cursor = self.__db.cursor()
            cursor.execute(query)
            self.__db.commit()
            user.SetMessage("Password was changed successfully!")
            cursor.close()
            return True
        except Exception as e:
            user.SetMessage(e)
            return False
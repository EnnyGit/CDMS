from dbContext import SqlDatabase

class AccountController:

    __db=None
    __user=None
    loggedinuser = None

    def __init__(self):
        self.__db= SqlDatabase.Connect()

    def __sendToDatabase(self, user):
        cursor = self.__db.cursor()
        query = f"INSERT INTO 'user' VALUES (NULL, '{user.GetUsername()}', '{user.GetPassword()}');"
        print(query)
        #cursor.execute("")

    def Save(self, user):
        if self.__sendToDatabase(user):
            pass

    def __isvalid(user):
        if user.GetFname() != "" and user.GetLname() !="" and user.GetUsername() !="" and user.GetPassword() != "" and user.GetEmail() !="":
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
        # Log here
    

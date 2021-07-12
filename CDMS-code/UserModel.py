class User:

    #attributes
    username  = ""
    password  = ""
    firstname = ""
    lastname  = ""
    email     = ""
    message   = ""


    #constructor
    def __init__(self):
        pass

    #setters
    def SetUsername(self, param):
        self.username = param
    
    def SetPassword(self, param):
        self.password = param

    def SetFname(self, param):
        self.firstname = param
    
    def SetLname(self, param):
        self.lastname = param

    def SetEmail(self, param):
        self.email = param

    def SetMessage(self, param):
        self.message = param

    #getters
    def GetUsername(self):
        return self.username

    def GetPassword(self):
        return self.password

    def GetFname(self):
        return self.firstname

    def GetLname(self):
        return self.lastname

    def GetEmail(self):
        return self.email

    def GetMessage(self):
        return self.message
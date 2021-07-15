class User:

    #constructor
    def __init__(self, id=None, username="", password="", firstname="", lastname="", registrationDate="", role=""):
        self.id = id
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.registrationDate = registrationDate
        self.role = role

    #setters
    def SetUsername(self, param):
        self.username = param
    
    def SetPassword(self, param):
        self.password = param

    def SetFname(self, param):
        self.firstname = param
    
    def SetLname(self, param):
        self.lastname = param

    def SetRole(self, param):
        self.role = param

    def SetRegistrationDate(self, param):
        self.registrationDate = param
        
    #getters
    def GetUsername(self):
        return self.username

    def GetPassword(self):
        return self.password

    def GetFname(self):
        return self.firstname

    def GetLname(self):
        return self.lastname

    def GetRole(self):
        return self.role

    def GetRegistrationDate(self):
        return self.registrationDate
from ValidationController import Validation

class User:

    #attributes
    username            = ""
    password            = ""
    firstname           = ""
    lastname            = ""
    email               = ""
    registrationDate    = ""
    role                = ""

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

    def GetEmail(self):
        return self.email

    def GetRole(self):
        return self.role

    def GetRegistrationDate(self):
        return self.registrationDate

        #TODO Move to view
    def inputFname(self):
        while True:
            userinput = input('Please input user\'s first name\n')
            if Validation.nameValidation(userinput) == True:
                self.firstname = userinput
                return
            elif len(userinput) > 20 or len(userinput) == 0:
                print("first name must be within 1-20 characters.\n")
            else:
                print("first name must only contain letters, spaces ( ) and hyphens (-)\n")

    #TODO Move to view
    def inputLname(self):
        while True:
            userinput = input('Please input user\'s last name\n')
            if Validation.nameValidation(userinput) == True:
                self.lastname = userinput
                return
            elif len(userinput) > 20 or len(userinput) == 0:
                print("last name must be within 1-20 characters.\n")
            else:
                print("last name must only contain letters, spaces ( ) and hyphens (-)\n")

    #TODO email regexes zijn naar / move to view
    def inputEmail(self):
        while True:
            userinput = input('Please input user\'s email\n')
            if Validation.emailValidation(userinput) == True:
                self.email = userinput
                return
            elif len(userinput) > 139 or len(userinput) < 6:
                print("email must be within 6-254 characters.\n")
            else:
                print("email must be of format 'example@example.com'\n")

    #TODO move to view
    def inputUsername(self):
        while True:
            userinput = input('Please input user\'s username\n')
            if Validation.emailValidation(userinput) == True:
                self.email = userinput
                return
            elif len(userinput) > 20 or len(userinput) < 5:
                print("username must be within 5-20 characters.\n")
            else:
                print("username must start with a letter and only contain alphanumeric characters and dashes (-), underscores (_), apostrophes ('), and periods (.)'\n")

    
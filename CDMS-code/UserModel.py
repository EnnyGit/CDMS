from ValidationController import Validation

class User:
    validator = Validation()

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
    def GetId(self):
        return self.id

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

    #TODO move to view
    #TODO Check if username exists
    def inputUsername(self):
        while True:
            userinput = input('Please input user\'s username\n')
            if self.validator.usernameValidation(userinput) == True:
                self.username = userinput
                return
            elif len(userinput) > 20 or len(userinput) < 5:
                print("username must be within 5-20 characters.\n")
            else:
                print("username must start with a letter and only contain alphanumeric characters and dashes (-), underscores (_), apostrophes ('), and periods (.)'\n")

    #TODO move to view
    def inputPassword(self):
        while True:
            userinput = input("Please input user\'s password, alphanumeric characters and special characters (~!@#$%^&*_-+\\|(){}[]:;'<>,.?/) are allowed\nPassword must contain at least one lowercase letter, uppercase letter, digit and special character\n")

            if self.validator.passwordValidation(userinput) == True:
                self.password = userinput
                return
            if len(userinput) > 30 or len(userinput) < 8:
                print("Password must be within 8-30 characters.\n")
            if not self.validator.containsLowercase(userinput):
                print("Password must contain a lowercase letter")
            if not self.validator.containsUppercase(userinput):
                print("Password must contain an uppercase letter")
            if not self.validator.containsSpecialCharacter(userinput):
                print("Password must contain a special character")
            if not self.validator.containsDigit(userinput):
                print("Password must contain a digit")

from ValidationController import Validation
from UserController import UserController
import Config

class UserView:
    validator = Validation()
    usercontroller = UserController()


    def inputFname(self, user):
        while True:
            userinput = input('Please input user\'s first name\n')
            if self.validator.nameValidation(userinput) == True:
                user.firstname = userinput
                return
            elif len(userinput) > 20 or len(userinput) == 0:
                print("first name must be within 1-20 characters.\n")
            else:
                print("first name must only contain letters, spaces ( ) and hyphens (-)\n")

    def inputLname(self, user):
        while True:
            userinput = input('Please input user\'s last name\n')
            if self.validator.nameValidation(userinput) == True:
                user.lastname = userinput
                return
            elif len(userinput) > 20 or len(userinput) == 0:
                print("last name must be within 1-20 characters.\n")
            else:
                print("last name must only contain letters, spaces ( ) and hyphens (-)\n")

    def inputUsername(self, user):
        while True:
            userinput = input('Please input user\'s username\n')
            if self.validator.usernameValidation(userinput) == True:
                user.username = userinput
                return
            elif len(userinput) > 20 or len(userinput) < 5:
                print("username must be within 5-20 characters.\n")
            else:
                print("username must start with a letter and only contain alphanumeric characters and dashes (-), underscores (_), apostrophes ('), and periods (.)'\n")

    def inputPassword(self, user):
        while True:
            userinput = input("Please input user\'s password, alphanumeric characters and special characters (~!@#$%^&*_-+\\|(){}[]:;'<>,.?/) are allowed\nPassword must contain at least one lowercase letter, uppercase letter, digit and special character\n")

            if self.validator.passwordValidation(userinput) == True:
                user.password = userinput
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

    def SetTempPassword(self, user):
        temppassword = self.NewTempPassword()
        print(f'Your new temporary password is: {temppassword}')
        user.SetPassword(temppassword)

    def updatePassword(self):
        while True:
            #TODO Log this
            currentpassword = input('Please enter your current password for authentication or type exit to return to the main menu.\n')
            if Config.loggedInUser.password == currentpassword:
                while True:
                    userinput = input("Please enter your new password, alphanumeric characters and special characters (~!@#$%^&*_-+\\|(){}[]:;'<>,.?/) are allowed\nPassword must contain at least one lowercase letter, uppercase letter, digit and special character\n")
                    #TODO log some stuff here?
                    if self.validator.passwordValidation(userinput) == True:
                        Config.loggedInUser.password = userinput
                        self.usercontroller.UpdateUser(Config.loggedInUser)
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
            elif currentpassword == 'exit':
                return

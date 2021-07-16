from ValidationController import Validation
from UserController import UserController
import Config

class UserView:
    validator = Validation()
    usercontroller = UserController()


    def inputFname(self, user):
        while True:
            userinput = input('\n First name: ')
            if self.validator.nameValidation(userinput) == True:
                user.firstname = userinput
                return
            elif len(userinput) > 20 or len(userinput) == 0:
                print(" ERROR: First name must be within 1-20 characters.\n")
            else:
                print(" ERROR: First name must only contain letters, spaces ( ) and hyphens (-)\n")

    def inputLname(self, user):
        while True:
            userinput = input('\n Last name: ')
            if self.validator.nameValidation(userinput) == True:
                user.lastname = userinput
                return
            elif len(userinput) > 20 or len(userinput) == 0:
                print(" ERROR: Last name must be within 1-20 characters.\n")
            else:
                print(" ERROR: Last name must only contain letters, spaces ( ) and hyphens (-)\n")

    def inputUsername(self, user):
        while True:
            userinput = input('\n Username: ')
            if self.validator.usernameValidation(userinput) == True:
                user.username = userinput
                return
            elif len(userinput) > 20 or len(userinput) < 5:
                print(" ERROR: Username must be within 5-20 characters.\n")
            else:
                print(" ERROR: Username must start with a letter and only contain alphanumeric characters and dashes (-), underscores (_), apostrophes ('), and periods (.)'\n")

    def inputPassword(self, user):
        while True:
            print("\n Alphanumeric characters and special characters are allowed\n Password must contain at least one lowercase letter, uppercase letter, digit and special character")
            userinput = input("\n Password: ")

            if self.validator.passwordValidation(userinput) == True:
                user.password = userinput
                return
            if len(userinput) > 30 or len(userinput) < 8:
                print(" ERROR: Password must be within 8-30 characters.\n")
            if not self.validator.containsLowercase(userinput):
                print(" ERROR: Password must contain a lowercase letter")
            if not self.validator.containsUppercase(userinput):
                print(" ERROR: Password must contain an uppercase letter")
            if not self.validator.containsSpecialCharacter(userinput):
                print(" ERROR: Password must contain a special character")
            if not self.validator.containsDigit(userinput):
                print(" ERROR: Password must contain a digit")

    def SetTempPassword(self, user):
        temppassword = self.NewTempPassword()
        print(f' INFO: Your new temporary password is: {temppassword}')
        user.SetPassword(temppassword)

    def updatePassword(self, user):
        while True:
            #TODO Log this
            print("\n Please enter your current password for authentication or type exit to return to the main menu.")
            currentpassword = input('\n Current Password: ')
            if user.password == currentpassword:
                while True:
                    print("\n Alphanumeric characters and special characters (~!@#$%^&*_-+\\|(){}[]:;'<>,.?/) are allowed\nPassword must contain at least one lowercase letter, uppercase letter, digit and special character")
                    userinput = input("\n New Password: ")
                    #TODO log some stuff here?
                    if self.validator.passwordValidation(userinput) == True:
                        user.password = userinput
                        self.usercontroller.UpdateUser(user)
                        return
                    if len(userinput) > 30 or len(userinput) < 8:
                        print(" ERROR: Password must be within 8-30 characters.\n")
                    if not self.validator.containsLowercase(userinput):
                        print(" ERROR: Password must contain a lowercase letter")
                    if not self.validator.containsUppercase(userinput):
                        print(" ERROR: Password must contain an uppercase letter")
                    if not self.validator.containsSpecialCharacter(userinput):
                        print(" ERROR: Password must contain a special character")
                    if not self.validator.containsDigit(userinput):
                        print(" ERROR: Password must contain a digit")
            elif currentpassword == 'exit':
                return

from ValidationController import Validation

class ClientView:
    validator = Validation()

    def inputFirstName(self, client):
        while True:
            userinput = input('Please input client\'s first name\n')
            if self.validator.nameValidation(userinput) == True:
                client.firstname = userinput
                return
            elif len(userinput) > 20 or len(userinput) == 0:
                print("first name must be within 1-20 characters.\n")
            else:
                print("first name must only contain letters, spaces ( ) and hyphens (-)\n")

    def inputLastName(self, client):
        while True:
            userinput = input('Please input client\'s last name\n')
            if self.validator.nameValidation(userinput) == True:
                client.lastname = userinput
                return
            elif len(userinput) > 20 or len(userinput) == 0:
                print("last name must be within 1-20 characters.\n")
            else:
                print("last name must only contain letters, spaces ( ) and hyphens (-)\n")

    def inputEmail(self, client):
        while True:
            userinput = input('Please input client\'s email\n')
            if self.validator.emailValidation(userinput) == True:
                client.email = userinput
                return
            elif len(userinput) > 139 or len(userinput) < 6:
                print("email must be within 6-254 characters.\n")
            else:
                print("email must be of format 'example@example.com'\n")

    def inputPhone(self, client):
        while True:
            userinput = input('Please input client\'s mobile phone number\n31-6-')
            if self.validator.phoneValidation(userinput) == True:
                client.phone = f'31-6-{userinput}'
                return
            elif len(userinput) > 8 or len(userinput) == 0:
                print("phone must be 8 characters.\n")
            else:
                print("phone must consist of only numbers\n")

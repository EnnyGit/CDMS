from AddressModel import Address
from ValidationController import Validation

class Client:

    def __init__(self, id=None, firstname='', lastname='', address='', email='',  phone = ''):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.email = email
        self.phone = phone

    # Setters
    def SetFname(self, param):
        slast = param

    def SetLname(self, param):
        self.lastname = param

    def SetAddress(self, param):
        self.address = param

    def SetEmail(self, param):
        self.email = param

    def SetPhone(self, param):
        self.phone = param

    # Getters
    def GetFname(self):
        return self.firstname

    def GetLname(self):
        return self.lastname

    def GetAddress(self):
        return self.address

    def GetEmail(self):
        return self.email

    def GetPhone(self):
        return self.phone

    #TODO Move to view
    def inputFirstName(self):
        while True:
            userinput = input('Please input client\'s first name\n')
            if Validation.nameValidation(userinput) == True:
                self.firstname = userinput
                return
            elif len(userinput) > 20 or len(userinput) == 0:
                print("first name must be within 1-20 characters.\n")
            else:
                print("first name must only contain letters, spaces ( ) and hyphens (-)\n")

    #TODO Move to view
    def inputLastName(self):
        while True:
            userinput = input('Please input client\'s last name\n')
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
            userinput = input('Please input client\'s email\n')
            if Validation.emailValidation(userinput) == True:
                self.email = userinput
                return
            elif len(userinput) > 139 or len(userinput) < 6:
                print("email must be within 6-254 characters.\n")
            else:
                print("email must be of format 'example@example.com'\n")

    #TODO move to view
    def inputPhone(self):
        while True:
            userinput = input('Please input client\'s mobile phone number\n31-6-')
            if Validation.phoneValidation(userinput) == True: #TODO fix
                self.phone = f'31-6-{userinput}'
                return
            elif len(userinput) > 8 or len(userinput) == 0:
                print("phone must be 8 characters.\n")
            else:
                print("phone must consist of only numbers\n")

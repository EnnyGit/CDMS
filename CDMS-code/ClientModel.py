from AddressModel import Address

class Client:

    firstname = ''
    lastname  = ''
    address   = ''
    email     = ''
    phone     = ''

    def __init__(self):
        pass

    # Setters
    def SetFname(self, param):
        self.firstname = param

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

#TODO Input validation / Move to view
def setName(self):
    self.fullname = input('Please input clients full name\n')

#TODO Input validation / Move to view
def setEmail(self):
    self.email = input('Please input clients email\n')

#TODO Input validation / Move to view
def setPhone(self):
    self.phone = input('Please input clients phone\n')

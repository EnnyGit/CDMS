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
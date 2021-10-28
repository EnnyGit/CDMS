class Client:

    def __init__(self, id=None, firstname='', lastname='', streetname='', housenumber='', zipcode='', city='', email='',  phone = ''):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.streetname = streetname
        self.housenumber = housenumber
        self.zipcode = zipcode
        self.city = city
        self.email = email
        self.phone = phone

    # Setters
    def SetFname(self, param):
        slast = param

    def SetLname(self, param):
        self.lastname = param

    def SetCity(self, param):
        self.city = param

    def SetStreetname(self, param):
        self.streetname = param

    def SetHousenumber(self, param):
        self.housenumber = param

    def SetZipcode(self, param):
        self.zipcode = param

    def SetEmail(self, param):
        self.email = param

    def SetPhone(self, param):
        self.phone = param

    # Getters
    def GetFname(self):
        return self.firstname

    def GetLname(self):
        return self.lastname

    def GetCity(self):
        return self.city

    def GetStreetname(self):
        return self.streetname

    def GetHousenumber(self):
        return self.housenumber

    def GetZipcode(self):
        return self.zipcode

    def GetEmail(self):
        return self.email

    def GetPhone(self):
        return self.phone
class Address():

    cities = ["New York", "Tokyo", "London", "Paris", "Sydney", "Signapore", "Los Angeles", "Toronto", "Amsterdam", "San Jose"]
    city = ''
    streetname = ''
    housenumber = ''
    zipcode = ''

    def __init__(self):
        pass

    #setters
    def SetCity(self, param):
        self.city = param

    def SetStreetname(self, param):
        self.streetname = param

    def SetHousenumber(self, param):
        self.housenumber = param

    def SetZipcode(self, param):
        self.zipcode = param

    #getters
    def GetCity(self):
        return self.city

    def GetStreetname(self):
        return self.streetname

    def GetHousenumber(self):
        return self.housenumber

    def GetZipcode(self):
        return self.zipcode

    def GetFullAddress(self):
        return f"{self.streetname} {self.housenumber}, {self.zipcode}, {self.city}"

#TODO Input validation / change to view
def inputStreetName(self):
    self.streetname = input('Please input clients street name')

#TODO Input validation / change to view
def inputHouseNumber(self):
    self.housenumber = input('Please input clients house number\n')

#TODO Input validation / change to view
def inputZipCode(self):
    self.zipcode = input('Please input clients zipcode\n')
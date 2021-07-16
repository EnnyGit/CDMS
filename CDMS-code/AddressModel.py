from ValidationController import Validation

class Address():

    cities = ["New York", "Tokyo", "London", "Paris", "Sydney", "Signapore", "Los Angeles", "Toronto", "Amsterdam", "San Jose"]

    #constructor
    def __init__(self, streetname, housenumber, zipcode, city):
        self.streetname = streetname
        self.housenumber = housenumber
        self.zipcode = zipcode
        self.city = city

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
        if (self.streetname == None or self.housenumber == None or self.zipcode == None or self.city == None):
            return ''
        return "{} {}, {}, {}".format(self.streetname, self.housenumber, self.zipcode, self.city)
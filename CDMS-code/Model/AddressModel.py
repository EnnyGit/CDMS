class Address():

    #constructor
    def __init__(self, streetname, housenumber, zipcode):
        self.streetname = streetname
        self.housenumber = housenumber
        self.zipcode = zipcode

    #private attributes
    streetname = ""
    housenumber = ""
    zipcode = ""
    city = ["New York", "Tokyo", "London", "Paris", "Sydney", "Signapore", "Los Angeles", "Toronto", "Amsterdam", "San Jose"]

    #setters
    def SetStreetname(self, param):
        self.streetname = param

    def SetHousenumber(self, param):
        self.housenumber = param

    def SetZipcode(self, param):
        self.zipcode = param

    #getters
    def GetStreetname(self):
        return self.streetname

    def GetHousenumber(self):
        return self.housenumber

    def GetZipcode(self):
        return self.Zipcode

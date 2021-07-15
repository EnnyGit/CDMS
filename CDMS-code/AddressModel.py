from ValidationController import Validation

class Address():

    cities = ["New York", "Tokyo", "London", "Paris", "Sydney", "Signapore", "Los Angeles", "Toronto", "Amsterdam", "San Jose"]

    #constructor
    def __init__(self, streetname, housenumber, zipcode):
        self.streetname = streetname
        self.housenumber = housenumber
        self.zipcode = zipcode

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

    #TODO Input validation
    def inputStreetName(self):
        while True:
            userinput = input('Please input clients street name\n')
            if Validation.streetNameValidation(userinput) == True: #TODO fix
                self.streetname = userinput
                return
            elif len(userinput) > 55 or len(userinput) == 0:
                print("streetname must be within 1-55 characters.")
            else:
                print("streetname must only contain the characters: [~!@#$%^&*_-+=` |\(){}[]:;'<>,.?/]")

    #TODO Input validation
    def inputHouseNumber(self):
        while True:
            userinput = input('Please input clients house number\n')
            if Validation.houseNumberValidation(userinput) == True: #TODO fix
                self.housenumber = userinput
                return
            elif len(userinput) > 6 or len(userinput) == 0:
                print("housenumber must be within 1-6 characters.")
            else:
                print("housenumber must be a number between 1-99999 with an optional letter (e.g. 123a)")

    #TODO Input validation
    def inputZipCode(self):
        while True:
            userinput = input('Please input clients zip code\n')
            if Validation.zipCodeValidation(userinput) == True: #TODO fix
                self.zipcode = userinput
                return
            elif len(userinput) > 6 or len(userinput) == 0:
                print("zipcode must be within 1-6 characters.")
            else:
                print("zipcode must be a number between 1-99999 with an optional letter (e.g. 123a)")

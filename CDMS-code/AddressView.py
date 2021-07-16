from ValidationController import Validation

class AddressView:
    validator = Validation()

    def inputStreetName(self, address):
        while True:
            userinput = input('\n Street name: ')
            if self.validator.streetNameValidation(userinput) == True:
                address.streetname = userinput
                return
            elif len(userinput) > 55 or len(userinput) == 0:
                print(" ERROR: Streetname must be within 1-55 characters.\n")
            else:
                print(" ERROR: Streetname must only contain the characters: [~!@#$%^&*_-+=` |\(){}[]:;'<>,.?/]\n")

    def inputHouseNumber(self, address):
        while True:
            userinput = input('\n House number: ')
            if self.validator.houseNumberValidation(userinput) == True:
                address.housenumber = userinput
                return
            elif len(userinput) > 6 or len(userinput) == 0:
                print(" ERROR: Housenumber must be within 1-6 characters.\n")
            else:
                print(" ERROR: Housenumber must be a number between 1-99999 with an optional letter (e.g. 123a)\n")

    def inputZipCode(self, address):
        while True:
            userinput = input('\n Zipcode: ')
            if self.validator.zipCodeValidation(userinput) == True:
                address.zipcode = userinput
                return
            elif len(userinput) > 6 or len(userinput) == 0:
                print(" ERROR: Zipcode must be within 1-6 characters.\n")
            else:
                print(" ERROR: Zipcode must be a number between 1000-9999 followed by two letters (e.g. 1234AB)\n")

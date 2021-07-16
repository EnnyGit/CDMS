from ValidationController import Validation

class AddressView:
    validator = Validation()

    def inputStreetName(self, address):
        while True:
            userinput = input('Please input clients street name\n')
            if self.validator.streetNameValidation(userinput) == True:
                address.streetname = userinput
                return
            elif len(userinput) > 55 or len(userinput) == 0:
                print("streetname must be within 1-55 characters.")
            else:
                print("streetname must only contain the characters: [~!@#$%^&*_-+=` |\(){}[]:;'<>,.?/]")

    def inputHouseNumber(self, address):
        while True:
            userinput = input('Please input clients house number\n')
            if self.validator.houseNumberValidation(userinput) == True:
                address.housenumber = userinput
                return
            elif len(userinput) > 6 or len(userinput) == 0:
                print("housenumber must be within 1-6 characters.")
            else:
                print("housenumber must be a number between 1-99999 with an optional letter (e.g. 123a)")

    def inputZipCode(self, address):
        while True:
            userinput = input('Please input clients zipcode\n')
            if self.validator.zipCodeValidation(userinput) == True:
                address.zipcode = userinput
                return
            elif len(userinput) > 6 or len(userinput) == 0:
                print("zipcode must be within 1-6 characters.")
            else:
                print("zipcode must be a number between 1000-9999 followed by two letters (e.g. 1234AB)")

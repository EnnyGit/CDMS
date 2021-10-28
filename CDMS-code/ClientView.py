from ValidationController import Validation

class ClientView:
    validator = Validation()
    cities = ["New York", "Tokyo", "London", "Paris", "Sydney", "Signapore", "Los Angeles", "Toronto", "Amsterdam", "San Jose"]

    def inputFirstName(self, client):
        while True:
            userinput = input('\n Input Firstname: ')
            if self.validator.nameValidation(userinput) == True:
                client.firstname = userinput
                return
            elif len(userinput) > 20 or len(userinput) == 0:
                print(" INFO: First name must be within 1-20 characters.\n")
            else:
                print(" INFO: First name must only contain letters, spaces ( ) and hyphens (-)\n")

    def inputLastName(self, client):
        while True:
            userinput = input('\n Input Lastname: ')
            if self.validator.nameValidation(userinput) == True:
                client.lastname = userinput
                return
            elif len(userinput) > 20 or len(userinput) == 0:
                print(" INFO: Last name must be within 1-20 characters.\n")
            else:
                print(" INFO: Last name must only contain letters, spaces ( ) and hyphens (-)\n")

    def inputEmail(self, client):
        while True:
            userinput = input('\n Input Email: ')
            if self.validator.emailValidation(userinput) == True:
                client.email = userinput
                return
            elif len(userinput) > 139 or len(userinput) < 6:
                print("  INFO: Email must be within 6-254 characters.\n")
            else:
                print(" INFO: Email must be of format 'example@example.com'\n")

    def inputPhone(self, client):
        while True:
            userinput = input(' Input mobile phone number: 31-6-')
            if self.validator.phoneValidation(userinput) == True:
                client.phone = f'31-6-{userinput}'
                return
            elif len(userinput) > 8 or len(userinput) == 0:
                print(" INFO: Phone must be 8 characters.\n")
            else:
                print(" INFO: Phone must consist of only numbers\n")

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


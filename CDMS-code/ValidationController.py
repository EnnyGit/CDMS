import re

class Validation:
    def __init__(self):
        pass

    def inputNumberIsInRange(self, userinput, min, max):
        while True:
            if userinput.isnumeric():
                if int(userinput) in range(min, max + 1):
                    return True
                else:
                    print("Input is not valid because it isn't in the range {}-{}".format(min, max))
                    return False
            else:
                print("Input is not valid because it isn't a number")
                return False

    def streetNameValidation(self, userinput):
        return bool(re.findall(r"^[0-9a-zA-Z~!@#$%^&*_\-+\\|(){}\[\]:;'<>,.?/ ]{1,55}$", userinput))

    def houseNumberValidation(self, userinput):
        return bool(re.findall("^[1-9]{1}[0-9]{0,4}[a-zA-Z]?$", userinput))

    def zipCodeValidation(self, userinput):
    	return bool(re.findall("^[1-9]{1}[0-9]{3}[a-zA-Z]{2}$", userinput))

    def nameValidation(self, userinput):
        return bool(re.findall("^[a-zA-Z \-]{1,20}$", userinput))

    def emailValidation(self, userinput):
        return bool(re.findall("^[\w!#$%&'*+\-/=?\^_`{|}~]+(\.[\w!#$%&'*+\-/=?\^_`{|}~]+)*@((([\-\w]+\.)+[a-zA-Z]{2,4})|(([0-9]{1,3}\.){3}[0-9]{1,3}))$", userinput))

    def phoneValidation(self, userinput):
        return bool(re.findall('^[0-9]{8}$', userinput))

    def usernameValidation(self, userinput):
        return bool(re.findall("^[a-zA-Z]{1}[a-zA-Z0-9\-_'.]{4,19}$", userinput))

    def containsLowercase(self, userinput):
        return bool(re.findall('[a-z]+', userinput))    

    def containsUppercase(self, userinput):
        return bool(re.findall('[A-Z]+', userinput))      

    def containsSpecialCharacter(self, userinput):
        return any(char in userinput for char in '''~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/''')

    def containsDigit(self, userinput):
        return bool(re.findall('[0-9]+', userinput))

    def passwordValidation(self, userinput):
        if self.containsDigit(userinput) and self.containsLowercase(userinput) == True and\
             self.containsSpecialCharacter(userinput) and self.containsLowercase(userinput):
            return bool(re.findall(r"^[0-9a-zA-Z~!@#$%^&*_\-+\\|(){}\[\]:;'<>,.?/]{8,30}$", userinput))
        else:
            return False
import re

class Validation:
    def __init__(self):
        pass
    
    def ValidateUsernamePassword(self, username, password):
        #TODO implement Username/password validation
        #TODO return false if wrong combination
        if (username == 'superadmin' and password == 'Admin!23'):
            return True
        else: 
            return False

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

    #TODO Make zipcode data all uppercase
    def zipCodeValidation(self, userinput):
    	return bool(re.findall("^[0-9]{4}[a-zA-Z]{2}$", userinput))

    def containsLowercase(self, userinput):
        return bool(re.findall('[a-z]+', userinput))    

    def containsUppercase(self, userinput):
        return bool(re.findall('[A-Z]+', userinput))      

    def containsSpecialCharacter(self, userinput):
        return any(char in userinput for char in '''~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/''')

    def passwordValidation(self, userinput):
        return bool(re.findall(r"^[0-9a-zA-Z~!@#$%^&*_\-+\\|(){}\[\]:;'<>,.?/]{8,30}$", userinput))


#TODO Remove test case
# validator = Validation()
# testcase = input('Please input test string\n')
# print(validator.containsLowercase(testcase))
# print(validator.containsUppercase(testcase))
# print(validator.containsSpecialCharacter(testcase))
# print(validator.passwordValidation(testcase))


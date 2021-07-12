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



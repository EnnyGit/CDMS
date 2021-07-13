import SanitationController as sanitation
import ValidationController as validation
import NavigationController as navigation

def Main():
    Login()
    while True:
        navigator.mainMenu()
        


def Login():
    while(True):
        print("\x1b[0;37;40mPlease log in before using the system\n")
        username = input("Please input username\n")
        sanitation.StringSanitation(username)

        
        password = input("Please input password\n")
        sanitation.StringSanitation(password)

        if(not validator.ValidateUsernamePassword(username, password)):
            print("\x1b[1;31;40mIncorrect username or password\n")
        elif(validator.ValidateUsernamePassword(username, password)):
            break

navigator = navigation.Navigator()
validator = validation.Validation()
Main()
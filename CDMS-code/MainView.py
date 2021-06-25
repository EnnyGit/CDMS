import SanitationController as sanitation
import ValidationController as validation

def Main():
    while(True):
        Login()
        MainMenu()
        


def Login():
    while(True):
        print("\x1b[0;37;40mPlease log in before using the system\n")
        username = input("Please input username\n")
        sanitation.StringSanitation(username)

        
        password = input("Please input password\n")
        sanitation.StringSanitation(password)

        if(not validation.ValidateUsernamePassword(username, password)):
            print("\x1b[1;31;40mIncorrect username or password\n")
        elif(validation.ValidateUsernamePassword(username, password)):
            break

def MainMenu():
    print('mainmenu')

Main()
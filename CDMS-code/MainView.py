import SanitationController as sanitation
import ValidationController as validation
import NavigationController as navigation
import AccountContoller as accountcontrol
from AccountView import AccountView
import Config
from LoggingController import LoggingController

def Main():
    Logger = LoggingController()
    while True:
        condition = AccountView.login()   
        if condition:
            break
    if Config.loggedInUser.role == 'admin'  or Config.loggedInUser.role == 'superadmin':
        if Logger.Alert() != None:
            print(Logger.Alert())
    while True:
        navigator.mainMenu()

navigator = navigation.Navigator()
validator = validation.Validation()
accountcontroller = accountcontrol.AccountController()
Main()
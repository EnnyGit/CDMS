from AccountView import AccountView
import Config
from LoggingController import LoggingController
import NavigationView as navigation

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
Main()
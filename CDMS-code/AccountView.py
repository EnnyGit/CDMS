from UserModel import User
from AccountContoller import AccountController
from ClientController import ClientController
from DatabaseController import DatabaseController
from datetime import date, datetime
from ClientModel import Client

import Config

class AccountView:

    u = User()
    c = Client()
    acc = AccountController()
    clientController = ClientController()
    database = DatabaseController()

    @staticmethod
    def login():
        print("----------Welcome-----------")
        AccountView.u.SetUsername(input("Please write your Username: "))
        AccountView.u.SetPassword(input("Please write your Password: "))
        return AccountView.acc.Login(AccountView.u)

    @staticmethod
    def registerUser():
        print("----------User Registration-----------")
        AccountView.u.SetUsername(input("Username: "))
        AccountView.u.SetPassword(input("Password: "))
        AccountView.u.SetFname(input("First Name: "))
        AccountView.u.SetLname(input("Last Name: "))
        AccountView.u.SetRegistrationDate(f"{date.today().strftime('%d-%m-%Y')}, {datetime.now().strftime('%H:%M:%S')}")
        AccountView.u.SetRole(input("Role: "))
        AccountView.acc.Save(AccountView.u)

    @staticmethod
    def registerClient():
        print("----------User Registration-----------")
        AccountView.c.SetFname(input("Firstname: "))
        AccountView.c.SetLname(input("Lastname: "))
        AccountView.c.SetAddress(input("add: "))
        AccountView.c.SetLname(input("Last Name: "))
        AccountView.c.SetRegistrationDate(f"{date.today().strftime('%d-%m-%Y')}, {datetime.now().strftime('%H:%M:%S')}")
        AccountView.c.SetRole(input("Role: "))
        AccountView.clientController.Save(AccountView.c)
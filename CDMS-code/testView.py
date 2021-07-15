from UserModel import User
from AccountContoller import AccountController
from ClientController import ClientController
from DatabaseController import DatabaseController
from datetime import date, datetime
from ClientModel import Client

class TestView:

    u = User()
    c = Client()
    acc = AccountController()
    clientController = ClientController()
    database = DatabaseController()

    @staticmethod
    def login():
        print("----------Welcome-----------")
        TestView.u.SetUsername(input("Please write your Username: "))
        TestView.u.SetPassword(input("Please write your Password: "))
        TestView.acc.Login(TestView.u)
        print(TestView.u.GetMessage())

    @staticmethod
    def registerUser():
        print("----------User Registration-----------")
        TestView.u.SetUsername(input("Username: "))
        TestView.u.SetPassword(input("Password: "))
        TestView.u.SetFname(input("First Name: "))
        TestView.u.SetLname(input("Last Name: "))
        TestView.u.SetRegistrationDate(f"{date.today().strftime('%d-%m-%Y')}, {datetime.now().strftime('%H:%M:%S')}")
        TestView.u.SetRole(input("Role: "))
        TestView.acc.Save(TestView.u)

    @staticmethod
    def registerClient():
        print("----------User Registration-----------")
        TestView.c.SetFname(input("Firstname: "))
        TestView.c.SetLname(input("Lastname: "))
        TestView.c.SetAddress(input("add: "))
        TestView.c.SetLname(input("Last Name: "))
        TestView.c.SetRegistrationDate(f"{date.today().strftime('%d-%m-%Y')}, {datetime.now().strftime('%H:%M:%S')}")
        TestView.c.SetRole(input("Role: "))
        TestView.clientController.Save(TestView.c)
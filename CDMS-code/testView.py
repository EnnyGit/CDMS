from UserModel import User
from AccountContoller import AccountController
from DatabaseController import DatabaseController
from datetime import date, datetime

class TestView:

    u = User()
    acc = AccountController()
    database = DatabaseController()

    @staticmethod
    def login():
        print("----------Welcome-----------")
        TestView.u.SetUsername(input("Please write your Username: "))
        TestView.u.SetPassword(input("Please write your Password: "))
        TestView.acc.Login(TestView.u)
        print(TestView.u.GetMessage())

    @staticmethod
    def register():
        acc = AccountController()
        print("----------User Registration-----------")
        TestView.u.SetUsername(input("Username: "))
        TestView.u.SetPassword(input("Password: "))
        TestView.u.SetFname(input("First Name: "))
        TestView.u.SetLname(input("Last Name: "))
        TestView.u.SetRegistrationDate(f"{date.today().strftime('%d-%m-%Y')}, {datetime.now().strftime('%H:%M:%S')}")
        TestView.u.SetRole(input("Role: "))
        acc.Save(TestView.u)

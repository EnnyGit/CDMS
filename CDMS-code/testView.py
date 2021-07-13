from UserModel import User
from AccountContoller import AccountController
from DatabaseController import DatabaseController

class TestView:
    u = User()
    acc = AccountController()
    database = DatabaseController()

    #database.ExecuteQuery("CREATE TABLE user (id INT,username text,password text)")
    #database.ExecuteQuery("INSERT INTO 'user' VALUES ('2', 'admin', 'admin123')")
    @staticmethod
    def login():
        print("----------Welcome-----------")
        TestView.u.SetUsername(input("Please write your Username: "))
        TestView.u.SetPassword(input("Please write your Password: "))
        TestView.acc.Login(TestView.u)
        print(TestView.u.GetMessage())

    @staticmethod
    def register():
        print("----------User Registration-----------")
        TestView.u.SetUsername(input("Please Choose your Username: "))
        TestView.u.SetPassword(input("Please create a new Password: "))
        #u.SetFname(input("Please write your First Name: "))
        #u.SetLname(input("Please write your Last Name: "))
        #u.SetEmail(input("Please write your Email: "))
        TestView.acc.Save(TestView.u)
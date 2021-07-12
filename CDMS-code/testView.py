from UserModel import User
from AccountContoller import AccountController
from DatabaseController import DatabaseController

u = User()
acc = AccountController()
database = DatabaseController()

#database.ExecuteQuery("CREATE TABLE user (id INT,username text,password text)")
#database.ExecuteQuery("INSERT INTO 'user' VALUES ('2', 'admin', 'admin123')")


#print("----------Welcome-----------")
#u.SetUsername(input("Please write your Username: "))
#u.SetPassword(input("Please write your Password: "))
#acc.Login(u)
#print(u.GetMessage())

print("----------User Registration-----------")
u.SetUsername(input("Please Choose your Username: "))
u.SetPassword(input("Please create a new Password: "))
#u.SetFname(input("Please write your First Name: "))
#u.SetLname(input("Please write your Last Name: "))
#u.SetEmail(input("Please write your Email: "))

acc.Save(u)
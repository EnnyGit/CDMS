from UserModel import User
from AccountContoller import AccountController
from DatabaseController import DatabaseController

u = User()
acc = AccountController()
database = DatabaseController()

# print("----------Welcome-----------") # -READ-
# u.SetUsername(input("Please write your Username: "))
# u.SetPassword(input("Please write your Password: "))
# acc.Login(u)
# print(u.GetMessage())

# print("----------User Registration-----------") # -CREATE-
# u.SetUsername(input("Please Choose your Username: "))
# u.SetPassword(input("Please create a new Password: "))
# acc.Save(u)
# print(u.GetMessage())

# print("----------Remove Account-----------") # -DELETE-
# u.SetUsername(input("Please Choose your Username: "))
# u.SetPassword(input("Please create a new Password: "))
# acc.Remove(u)
# print(u.GetMessage())

print("----------Welcome-----------") # -UPDATE-
u.SetUsername(input("Please write your Username: "))
u.SetPassword(input("Please write your Password: "))
acc.ChangePassword(u)
print(u.GetMessage())
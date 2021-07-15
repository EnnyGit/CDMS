from dbContext import SqlDatabase
import Config


class ClientController:

    __db=None

    def __init__(self):
        self.__db= SqlDatabase.Connect()

    def __sendToDatabase(self, user):
        try:
            cursor = self.__db.cursor()
            query = f"INSERT INTO 'user' VALUES (NULL, '{user.GetUsername()}', '{user.GetPassword()}', '{user.GetFname()}', '{user.GetLname()}', '{user.GetRegistrationDate()}', '{user.GetRole()}');"
            cursor.execute(query)
            self.__db.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False

    def __isAuthentic(self, client):
        cursor = self.__db.cursor()
        cursor.execute(f"SELECT id FROM 'client' WHERE firstname = '{client.GetFname()}' AND lastname = '{client.GetLname()}'")
        record = cursor.fetchone()
        if record!=None:
            return True
        return False

    def Save(self, user):
        if self.__isValid(user):
            if self.__sendToDatabase(user):
                Config.loggedInUser = user
                print(f"User {user.GetUsername()} was registered successfully")
        else:
            print("Please fill in all  the fields!")
            

    def __isValid(self, user):
        if user.GetUsername() !="" and user.GetPassword() != "":
            return True
        return False

    def Remove(self, user):
        if self.__isValid(user):
            if self.__isAuthentic(user):
                if self.__DelUser(user):
                    print(f"User {user.GetUsername()}  was deleted successfully")
            else:
                print("Client with these credentials does not exist!")
        else:
            print("Please write a firstname and a lastname")

    def __DelUser(self, client):
        try:
            cursor = self.__db.cursor()
            query = f"DELETE FROM 'client' WHERE username = '{client.GetFname()}' AND lastname = '{client.GetLname}'"
            cursor.execute(query)
            self.__db.commit()
            return True
        except Exception as e:
            print(e)
            return False      
        finally:
            cursor.close()  

    def UpdatePhone(self, client):
        client.SetPhone(input("New phonenumber: "))
        query = f"UPDATE 'client' SET phone = '{client.GetPhone()}' WHERE firstname = '{client.GetFname()}' AND lastname = '{client.GetLname()}'"
        try:
            cursor = self.__db.cursor()
            cursor.execute(query)
            self.__db.commit()
            print("Phonenumber was changed successfully!")
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False
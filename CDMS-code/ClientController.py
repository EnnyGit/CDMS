from dbContext import SqlDatabase
from ClientModel import Client
import Config


class ClientController:

    __db=None

    def __init__(self):
        self.__db= SqlDatabase.Connect()

    def __sendToDatabase(self, client):
        try:
            cursor = self.__db.cursor()
            query = f"INSERT INTO 'client' VALUES (NULL, '{client.GetFname()}', '{client.GetLname()}', '{client.GetAddress()}', '{client.GetEmail()}', '{client.GetPhone()}');"
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

    def SetSelectedInClientData(self, client):
        try:
            cursor = self.__db.cursor()
            query = f"SELECT * FROM 'client' WHERE firstname = '{client.GetFname()}' AND lastname = '{client.GetLname()}'"
            cursor.execute(query)
            dbData = cursor.fetchone()
            dbClient = Client(dbData[0], dbData[1], dbData[2], dbData[3], dbData[4], dbData[5])
            Config.selectedClient = dbClient
            print("TEST: " + Config.selectedClient.phone)
        except Exception as e:
            print("ClientController Line 42: " + e)

    def GetClientByName(self, param):
        try:
            clientList = []
            cursor = self.__db.cursor()
            query = f"SELECT * FROM 'client' WHERE firstname || ' ' || lastname LIKE '%{param}%'"
            cursor.execute(query)
            dbData = cursor.fetchall()
            for client in dbData:
                clientList.append(Client(client[0], client[1], client[2], client[3], client[4], client[5]))
            return clientList
        except Exception as e:
            print("ClientController Line 56: " , e)

    def GetClientByEmail(self, param):
        try:
            clientList = []
            cursor = self.__db.cursor()
            query = f"SELECT * FROM 'client' WHERE email LIKE '%{param}%'"
            cursor.execute(query)
            dbData = cursor.fetchall()
            for client in dbData:
                clientList.append(Client(client[0], client[1], client[2], client[3], client[4], client[5]))
            return clientList
        except Exception as e:
            print("ClientController Line 69: " , e)

    def Save(self, client):
        if self.__isValid(client):
            if self.__sendToDatabase(client):
                print(f"Client {client.GetFname()} {client.GetLname()} was registered successfully")
        else:
            print("Please fill in all the fields!")
            

    def __isValid(self, user):
        if user.GetFname() !="" and user.GetLname() != "":
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

    def UpdateClient(self, client, id):
        client.SetPhone(input("New phonenumber: "))
        query = f"UPDATE 'client' SET firstname = '{client.GetFname()}', lastname = '{client.GetLname()}', address = '{client.GetAddress()}', email = '{client.GetEmail()}', phone = '{client.GetPhone()}' WHERE id = '{client.GetId()}'"
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



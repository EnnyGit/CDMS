from dbContext import SqlDatabase
from ClientModel import Client
from LogModel import Log
from LoggingController import LoggingController
import Config


class ClientController:
    __logger=None
    __db=None

    def __init__(self):
        self.__db= SqlDatabase.Connect()
        self.__logger= LoggingController()

    def __sendToDatabase(self, client):
        try:
            cursor = self.__db.cursor()
            query = f"INSERT INTO 'client' VALUES ('{client.GetFname()}', '{client.GetLname()}', '{client.GetStreetname()}', '{client.GetHousenumber()}', '{client.GetZipcode()}', '{client.GetCity()}', '{client.GetEmail()}', '{client.GetPhone()}');"
            cursor.execute(query)
            self.__db.commit()
            cursor.close()
            self.__logger.Log(Log(
                suspicious="No",
                description="New client is created",
                information=f"Name: {client.GetFname()}"
            ))
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
                clientList.append(Client(client[0], client[1], client[2], client[3], client[4], client[5], client[6], client[7], client[8]))
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
                clientList.append(Client(client[0], client[1], client[2], client[3], client[4], client[5], client[6], client[7], client[8]))
            return clientList
        except Exception as e:
            print("ClientController Line 69: " , e)

    def Save(self, client):
        if self.__isValid(client):
            if self.__sendToDatabase(client):
                print(f"Client {client.GetFname()} {client.GetLname()} was registered successfully")
        else:
            print(" INFO: Please fill in all the fields!\n")
            

    def __isValid(self, client):
        if client.GetFname() !="" and client.GetLname() != "":
            return True
        return False

    def Remove(self, client):
        if self.__isValid(client):
            if self.__isAuthentic(client):
                if self.__DelClient(client):
                    print(f"Client {client.GetFname()} {client.GetLname()} was deleted successfully")
                    self.__logger.Log(Log(
                        suspicious="No",
                        description=f"Client is deleted",
                        information=f"Client \"{client.GetFname()} {client.GetLname()}\" is deleted"
                    ))
            else:
                print(" INFO: Client with these credentials does not exist!\n")
        else:
            print(" INFO: Please write a firstname and a lastname\n")

    def __DelClient(self, client):
        try:
            cursor = self.__db.cursor()
            query = f"DELETE FROM 'client' WHERE firstname = '{client.GetFname()}' AND lastname = '{client.GetLname}'"
            cursor.execute(query)
            self.__db.commit()
            return True
        except Exception as e:
            print(e)
            return False      
        finally:
            cursor.close()  

    def UpdateClient(self, client, id):
        client.SetPhone(input(" New phonenumber: "))
        query = f"UPDATE 'client' SET firstname = '{client.GetFname()}', lastname = '{client.GetLname()}', streetname = '{client.GetStreetname()}', housenumber = '{client.GetHousenumber()}', zipcode = '{client.GetZipcode()}', city = '{client.GetCity()}', email = '{client.GetEmail()}', phone = '{client.GetPhone()}' WHERE id = '{client.GetId()}'"
        try:
            cursor = self.__db.cursor()
            cursor.execute(query)
            self.__db.commit()
            print(" INFO: Phonenumber was changed successfully!\n")
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False



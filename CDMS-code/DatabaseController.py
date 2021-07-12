from dbContext import SqlDatabase

class DatabaseController:

    __db=None
    __user=None

    def __init__(self):
        self.__db= SqlDatabase.Connect()

    def ExecuteQuery(self, query):
        cursor = self.__db.cursor()
        cursor.execute(query)
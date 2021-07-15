from dbContext import SqlDatabase
from csv import DictWriter, DictReader

class LoggingController:

    __log       = None
    __filename  = "logs.csv"
    __fieldnames= ['id','username', 'date', 'time', 'description', 'information', 'suspicious', 'read']

    def __init__(self):
        pass

    def Log(self, log):
        try:
            with open('logs.csv', 'a+', newline='') as csvfile:
                dictWriter = DictWriter(csvfile, fieldnames=self.__fieldnames)
                dictWriter.writerow({
                    'id': log.id,
                    'username': log.username,
                    'date': log.date,
                    'time': log.time,
                    'description': log.description,
                    'information': log.information,
                    'suspicious': log.suspicious,
                    'read': log.read
                })
        except Exception as e:
            print(e)
            return False

    def Alert():
        # Alert unread suspicious activities, once a admin is logged in
        pass

    def GetAllLogs(self):
        try:
            with open('logs.csv', mode='r') as csvfile:
                dictReader = DictReader(csvfile)
                lineCount = 0
                for row in dictReader:
                    if lineCount == 0:
                        print(f'Colunm names are: {", ".join(row)}')
                        lineCount += 1
                    print(f"dddd {row['username']} is the username and {row['date']} is the date")
                    lineCount += 1
                print(f'Processed {lineCount} lines')
        except Exception as e:
            print(e)
            return False

    def CalculateId(self):
        try:
            with open('logs.csv', mode='r') as csvfile:
                dictReader = DictReader(csvfile)
                calculateId = 1
                for row in dictReader:
                    calculateId += 1
                return calculateId
        except Exception as e:
            print(e)
            return False

    def GetLogs(self, amount):
        pass

    def GetAllUnreadLogs():
        pass
from dbContext import SqlDatabase
from csv import DictWriter, DictReader
from EncryptionController import EncryptionController 

class LoggingController:

    __log       = None
    __filename  = "logs.csv"
    __fieldnames= ['id','username', 'date', 'time', 'description', 'information', 'suspicious', 'read']
    __encrypt   = EncryptionController()

    def __init__(self):
        pass

    def Log(self, log):
        try:
            encryptedLog = self.__EncryptLog(log)
            with open('logs.csv', 'a+', newline='') as csvfile:
                dictWriter = DictWriter(csvfile, fieldnames=self.__fieldnames)
                dictWriter.writerow({
                    'id': encryptedLog.id,
                    'username': encryptedLog.username,
                    'date': encryptedLog.date,
                    'time': encryptedLog.time,
                    'description': encryptedLog.description,
                    'information': encryptedLog.information,
                    'suspicious': encryptedLog.suspicious,
                    'read': encryptedLog.read
                })
        except Exception as e:
            print(e)
            return False

    def Alert():
        # Alert unread suspicious activities, once a admin is logged in
        pass

    def __EncryptLog(self, log):
        log.username = self.__encrypt.CaesarCipher(log.username)
        log.date = self.__encrypt.CaesarCipher(log.date)
        log.time = self.__encrypt.CaesarCipher(log.time)
        log.description = self.__encrypt.CaesarCipher(log.description)
        log.information = self.__encrypt.CaesarCipher(log.information)
        log.suspicious = self.__encrypt.CaesarCipher(log.suspicious)
        log.read = self.__encrypt.CaesarCipher(log.read)
        return log

    def __DecryptLog(self, log):
        log.username = self.__encrypt.CaesarDecipher(log.username)
        log.date = self.__encrypt.CaesarDecipher(log.date)
        log.time = self.__encrypt.CaesarDecipher(log.time)
        log.description = self.__encrypt.CaesarDecipher(log.description)
        log.information = self.__encrypt.CaesarDecipher(log.information)
        log.suspicious = self.__encrypt.CaesarDecipher(log.suspicious)
        log.read = self.__encrypt.CaesarDecipher(log.read)
        return log

    def GetAllLogs(self):
        try:
            with open('logs.csv', mode='r') as csvfile:
                dictReader = DictReader(csvfile)
                logs = []
                lineCount = 0
                for log in dictReader:
                    if lineCount > 0:
                        logs.append(self.__DecryptLog(log))
                    lineCount += 1
                return logs
        except Exception as e:
            print(e)
            return False

    def PrintAllLogs(self, logs):
        fields = ['id','username', 'date', 'time', 'description', 'information', 'suspicious', 'read']
        for log in logs:
            if lineCount == 0:
                print(f"{fields[0]:4}| {fields[1]:10}| {fields[2]:10}| {fields[3]:8}| {fields[4]:19}| {fields[5]:65}| {fields[6]:11}| {fields[7]}")
                lineCount += 1
            print(f"%-{log['id']:2}| {log['username']:10}| {log['date']:10}| {log['time']:8}| {log['description']:19}| {log['information']:65}| {log['suspicious']:11}| {log['read']}")
            lineCount += 1

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
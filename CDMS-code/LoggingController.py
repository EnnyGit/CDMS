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

    def Alert(self):
        numberOfAlerts = 0
        unreadLogs = self.GetAllUnreadLogs()
        for log in unreadLogs:
            if log['suspicious'] == "Yes":
                numberOfAlerts += 1
        if numberOfAlerts > 0:
            return f"WARNING: You have {numberOfAlerts} unread suspicious logs !!"

    def __EncryptLog(self, log):
        log.username = self.__encrypt.CaesarCipher(log.username)
        log.date = self.__encrypt.CaesarCipher(log.date)
        log.time = self.__encrypt.CaesarCipher(log.time)
        log.description = self.__encrypt.CaesarCipher(log.description)
        log.information = self.__encrypt.CaesarCipher(log.information)
        log.suspicious = self.__encrypt.CaesarCipher(log.suspicious)
        log.read = self.__encrypt.CaesarCipher(log.read)
        return log

    def __EncryptDictLog(self, log):
        log['username'] = self.__encrypt.CaesarCipher(log['username'])
        log['date'] = self.__encrypt.CaesarCipher(log['date'])
        log['time'] = self.__encrypt.CaesarCipher(log['time'])
        log['description'] = self.__encrypt.CaesarCipher(log['description'])
        log['information'] = self.__encrypt.CaesarCipher(log['information'])
        log['suspicious'] = self.__encrypt.CaesarCipher(log['suspicious'])
        log['read'] = self.__encrypt.CaesarCipher(log['read'])
        return log

    def __DecryptLog(self, log):
        log['username'] = self.__encrypt.CaesarDecipher(log['username'])
        log['date'] = self.__encrypt.CaesarDecipher(log['date'])
        log['time'] = self.__encrypt.CaesarDecipher(log['time'])
        log['description'] = self.__encrypt.CaesarDecipher(log['description'])
        log['information'] = self.__encrypt.CaesarDecipher(log['information'])
        log['suspicious'] = self.__encrypt.CaesarDecipher(log['suspicious'])
        log['read'] = self.__encrypt.CaesarDecipher(log['read'])
        return log

    def GetAllLogs(self):
        try:
            with open('logs.csv', mode='r') as csvfile:
                dictReader = DictReader(csvfile)
                logs = []
                lineCount = 0
                for log in dictReader:
                    logs.append(self.__DecryptLog(log))
                    lineCount += 1
                return logs
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

    def ChangeLogsToRead(self):
        logs = self.GetAllLogs()
        try:
            with open('logs.csv', 'w', newline='') as csvfile:
                dictWriter = DictWriter(csvfile, fieldnames=self.__fieldnames)
                dictWriter.writeheader()
                for log in logs:
                    log['read'] = "Yes"
                    encryptedLog = encryptedLog = self.__EncryptDictLog(log)
                    dictWriter.writerow({
                        'id': encryptedLog['id'],
                        'username': encryptedLog['username'],
                        'date': encryptedLog['date'],
                        'time': encryptedLog['time'],
                        'description': encryptedLog['description'],
                        'information': encryptedLog['information'],
                        'suspicious': encryptedLog['suspicious'],
                        'read': encryptedLog['read']
                    })
        except Exception as e:
            print(e)
            return False

    def GetAllUnreadLogs(self):
        logs = self.GetAllLogs()
        unreadLogs = []
        for log in logs:
            if log['read'] == "No":
                unreadLogs.append(log)
        return unreadLogs
        
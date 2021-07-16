from LoggingController import LoggingController
from LogModel import Log

class LogView:

    Logger = LoggingController()

    def PrintAllLogs(self):
        Logs = self.Logger.GetAllLogs()
        fields = ['id','username', 'date', 'time', 'description', 'information', 'suspicious', 'read']
        lineCount = 0
        print(f"{fields[0]:4}| {fields[1]:10}| {fields[2]:10}| {fields[3]:8}| {fields[4]:19}| {fields[5]:65}| {fields[6]:11}| {fields[7]}")
        for log in Logs:
            print(f"{log['id']:4}| {log['username']:10}| {log['date']:10}| {log['time']:8}| {log['description']:19}| {log['information']:65}| {log['suspicious']:11}| {log['read']}")
            lineCount += 1
        self.Logger.ChangeLogsToRead()

Logger = LoggingController()
# Log = Log(
#     suspicious="Yes",
#     description="Unsuccessful login",
#     information="Password `admin234` is tried in combination with username `admin`"
# )
Logger.Log(Log(
    suspicious="Yes",
    description="Unsuccessful login",
    information="Password `admin234` is tried in combination with username `admin`"
))

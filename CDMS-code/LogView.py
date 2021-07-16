from LoggingController import LoggingController
from LogModel import Log

class LogView:

    Logger = LoggingController()

    def PrintAllLogs(self):
        Logs = self.Logger.GetAllLogs()
        fields = ['No','Username', 'Date', 'Time', 'Description of Activity', 'Additional Information', 'Suspicious', 'read']
        lineCount = 0
        print(f"\n {fields[0]:4}| {fields[1]:10}| {fields[2]:10}| {fields[3]:8}| {fields[4]:25}| {fields[5]:80}| {fields[6]:11}")
        for log in Logs:
            print(f" {log['id']:4}| {log['username']:10}| {log['date']:10}| {log['time']:8}| {log['description']:25}| {log['information']:80}| {log['suspicious']:11}")
            lineCount += 1
        print("-------------------------------------------------------------------[ End of Log ]--------------------------------------------------------------------\n")
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

from LogModel import Log
from LoggingController import LoggingController

Logger = LoggingController()

# Blablalba non suspicious log blababla
Log = Log(
    suspicious="Yes",
    description="Unsuccessful login",
    information="Password `admin234` is tried in combination with username `admin`"
)
#Logger.Log(Log)




Logs = Logger.GetAllLogs()
Logger.PrintAllLogs(Logs)
from LogModel import Log
from LoggingController import LoggingController
from DatabaseController import DatabaseController

Logger = LoggingController()
database = DatabaseController()

# Blablalba non suspicious log blababla
Log = Log(
    suspicious="No",
    description="Unsuccessful login",
    information="Password `admin234` is tried in combination with username `admin`"
)
Logger.Log(Log)
#Logger.GetAllLogs()
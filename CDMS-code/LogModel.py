from datetime import date, datetime
from LoggingController import LoggingController

class Log:

    _controller = LoggingController()
    id          = ""
    username    = ""
    date        = ""
    time        = ""
    description = ""
    information = ""
    suspicious  = ""
    read        = ""

    def __init__(self, description, information, suspicious):
        self.id = self._controller.CalculateId()
        self.username = "Admin"
        self.date = date.today().strftime("%d-%m-%Y")
        self.time = datetime.now().strftime("%H:%M:%S")
        self.description = description
        self.information = information
        self.suspicious = suspicious
        self.read = "No"


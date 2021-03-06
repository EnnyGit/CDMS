from datetime import date, datetime
from LoggingController import LoggingController
import Config

class Log:

    __controller = LoggingController()

    def __init__(self, description, information, suspicious):
        self.id = self.__controller.CalculateId()
        self.username = Config.currentUsername
        self.date = date.today().strftime("%d-%m-%Y")
        self.time = datetime.now().strftime("%H:%M:%S")
        self.description = description
        self.information = information
        self.suspicious = suspicious
        self.read = "No"


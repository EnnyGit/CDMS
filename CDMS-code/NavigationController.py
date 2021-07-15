import ValidationController as validation
from AccountContoller import AccountController
from ClientModel import Client
from AddressModel import Address
import Config

class Navigator:
    currentClient = Client()

    def __init__(self):
        self.validator = validation.Validation()

    def switchfunction(self, options):
        while True:
            counter = 1
            for o in options:
                print('{}. {}'.format(counter, o[0]))
                counter += 1
            userinput = input()
            if(self.validator.inputNumberIsInRange(userinput, 1, len(options))):
                func = options[int(userinput) - 1][1]
                func()
                if(int(userinput) == len(options)):
                    return

    def mainMenu(self):
        options = [
            ('Search client', self.searchClient),
            ('Register new client', self.registerNewClient),
            ('Update own password', self.placeHolder),
            ('Search advisors', self.searchAdvisor),
        ]

        if Config.loggedInUser.role == 'admin'  or Config.loggedInUser.role == 'superadmin': #TODO replace with better access rights check
            options.append(('Register new advisor', self.placeHolder))
            options.append(('Administration menu', self.administrationMenu))
        if Config.loggedInUser.role == 'superadmin':  #TODO replace with access rights check
            options.append(('Register new system adminitrator', self.placeHolder))
            options.append(('Search administrators', self.searchAdministrators))

        options.append(('Exit', exit))

        self.switchfunction(options)

    def searchClient(self):
        options = [
            ('Search client by name', self.placeHolder),
            ('Search client by email', self.placeHolder),
            ('Search client by username', self.placeHolder),
            ('Return to main menu', self.skip)
        ]

        self.switchfunction(options)

    def searchAdvisor(self):
        options = [
            ('Search advisor by name', self.placeHolder),
            ('Search advisor by email', self.placeHolder),
            ('Search advisor by username', self.placeHolder),
            ('Return to main menu', self.skip)
        ]

        self.switchfunction(options)

    def searchAdministrators(self):
        options = [
            ('Search administrator by name', self.placeHolder),
            ('Search administrator by email', self.placeHolder),
            ('Search administrator by username', self.placeHolder),
            ('Return to main menu', self.skip)
        ]

        self.switchfunction(options)

    def administrationMenu(self):
        options = [
            ('Check list of users/roles', self.placeHolder),
            ('Make system backup', self.placeHolder),
            ('Check log files', self.placeHolder),
            ('Return to main menu', self.skip)
        ]

        self.switchfunction(options)

    def registerNewClient(self):
        self.currentClient = Client()
        self.currentClient.address = Address(None, None, None)
        while True:
            options = [
                ('Name:              {}'.format(self.currentClient.fullname), self.currentClient.setName), #TODO split in first/last name
                ('Address:           {}'.format(self.currentClient.address.GetFullAddress()), self.addAddress), #TODO
                ('Email address:     {}'.format(self.currentClient.email), self.currentClient.setEmail),
                ('Phone number:      {}'.format(self.currentClient.phone), self.currentClient.setPhone),
                ('Confirm changes', self.placeHolder),#TODO Implement saving client to database                
                ('Return to main menu', self.skip)
            ]
            exit = self.switchfunctionInput(options, False)
            if exit == True:
                return

    def addAddress(self):
        while True:
            options = [
                ('Streetname        {}'.format(self.currentClient.address.streetname), self.currentClient.address.inputStreetName),
                ('Housenumber       {}'.format(self.currentClient.address.housenumber), self.currentClient.address.inputHouseNumber),
                ('Zipcodde          {}'.format(self.currentClient.address.zipcode), self.currentClient.address.inputZipCode),
                ('City              {}'.format(self.currentClient.address.city), self.addCity), #TODO Implement
                ('Return to client', self.skip)
            ]
            exit = self.switchfunctionInput(options, False)
            if exit == True:
                return

    def addCity(self):
        while True:
            options = [
                ("New York", lambda: self.currentClient.address.SetCity("New York")),
                ("Tokyo", lambda: self.currentClient.address.SetCity("Tokyo")),
                ("London", lambda: self.currentClient.address.SetCity("London")),
                ("Paris", lambda: self.currentClient.address.SetCity("Paris")),
                ("Sydney", lambda: self.currentClient.address.SetCity("Sydney")),
                ("Signapore", lambda: self.currentClient.address.SetCity("Signapore")),
                ("Los Angeles", lambda: self.currentClient.address.SetCity("Los Angeles")),
                ("Toronto", lambda: self.currentClient.address.SetCity("Toronto")),
                ("Amsterdam", lambda: self.currentClient.address.SetCity("Amsterdam")),
                ("San Jose", lambda: self.currentClient.address.SetCity("San Jose"))
            ]
            options.append(('Return to address', self.skip))
            exit = self.switchfunctionInput(options, True)
            if exit == True:
                return
        

    def switchfunctionInput(self, options, returntype):
        counter = 1
        for o in options:
            print('{}. {}'.format(counter, o[0]))
            counter += 1
        userinput = input()
        if(self.validator.inputNumberIsInRange(userinput, 1, len(options))):
            func = options[int(userinput) - 1][1]
            func()
            if(int(userinput) == len(options)) or returntype == True:
                return True

    def placeHolder(self):
        print('If you see this the method is not finished yet.')

    def skip(self):
        return
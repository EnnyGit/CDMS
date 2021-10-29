from UserView import UserView
from ClientView import ClientView
from UserController import UserController
import ValidationController as validation
from AccountController import AccountController
from ClientController import ClientController
from UserController import UserController
from ClientModel import Client
from UserModel import User
from FileController import FileController
from LogView import LogView
import Config

class Navigator:
    currentClient = Client()
    currentUser = User()
    clientController = ClientController()
    accountController = AccountController()
    userController = UserController()
    fileController = FileController()
    clientView = ClientView()
    userView = UserView()
    logview = LogView()

    def __init__(self):
        self.validator = validation.Validation()

    def switchfunction(self, options):
        while True:
            counter = 1
            for o in options:
                print(' {}. {}'.format(counter, o[0]))
                counter += 1
            userinput = input("\n Option: ")
            if(self.validator.inputNumberIsInRange(userinput, 1, len(options))):
                func = options[int(userinput) - 1][1]
                func()
                if(int(userinput) == len(options)):
                    return

    def mainMenu(self):
        print('--------------------[ Main menu ]--------------------\n')
        print(' Please choose an option by typing the number\n')
        options = [          
            ('Client  - Registration', self.registerNewClient),
            ('Client  - Search', self.searchClient),
            ('Update password', lambda: self.userView.updatePassword(Config.loggedInUser)),
        ]
        if Config.loggedInUser.role == 'admin'  or Config.loggedInUser.role == 'superadmin':
            options = [          
                ('Client  - Registration', self.registerNewClient),
                ('Advisor - Registration', lambda: self.registerNewUser('advisor')),
                ('Client  - Search', self.searchClient),
                ('Advisor - Search', self.searchAdvisor),
                ('Update password', lambda: self.userView.updatePassword(Config.loggedInUser)),
                ('Tools', self.administrationMenu)
            ]
        if Config.loggedInUser.role == 'superadmin':
            options = [          
                ('Client  - Registration', self.registerNewClient),
                ('Advisor - Registration', lambda: self.registerNewUser('advisor')),
                ('Admin   - Registration', lambda: self.registerNewUser('admin')),
                ('Client  - Search', self.searchClient),
                ('Advisor - Search', self.searchAdvisor),
                ('Admin   - Search', self.searchAdministrators),
                ('Update password', lambda: self.userView.updatePassword(Config.loggedInUser)),
                ('Tools', self.administrationMenu)
            ]
        options.append(('Exit', exit))
        self.switchfunction(options)

    def searchClient(self):
        print('\n----------------[ Search for a Client ]----------------\n')
        options = [
            ('Search by name', self.SearchClientByName),
            ('Search by email', self.SearchClientByEmail),
            ('Show all Clients', self.ShowClients),
            ('RETURN', self.skip)
        ]

        self.switchfunction(options)

    def searchAdvisor(self):
        print('\n----------------[ Search for a Advisor ]----------------\n')
        options = [
            ('Search by name', lambda: self.SearchUserByName('advisor')),
            ('Search by username', lambda: self.SearchUserByUsername('advisor')),
            ('Show all Advisors', lambda: self.ShowAllUsers('advisor')),
            ('RETURN', self.skip)
        ]

        self.switchfunction(options)

    def searchAdministrators(self):
        print('\n----------------[ Search for an Administrator ]----------------\n')
        options = [
            ('Search by name',lambda: self.SearchUserByName('admin')),
            ('Search by username', lambda: self.SearchUserByUsername('admin')),
            ('Show all Admins', lambda: self.ShowAllUsers('admin')),
            ('RETURN', self.skip)
        ]

        self.switchfunction(options)

    def administrationMenu(self):
        print('\n----------------[ Tools ]----------------\n')
        options = [
            ('Make Backup', self.fileController.CreateBackup),
            ('Show Log', self.logview.PrintAllLogs),
            ('RETURN', self.skip)
        ]

        self.switchfunction(options)

    def registerNewClient(self):
        self.currentClient = Client()
        while True:
            print('------------------[ Register new client ]------------------\n')
            print(' Choose the option of the value you want to change, then choose confirm to save\n')
            options = [
                ('First name:         {}'.format(self.currentClient.GetFname()), lambda: self.clientView.inputFirstName(self.currentClient)),
                ('Last name:          {}'.format(self.currentClient.GetLname()), lambda: self.clientView.inputLastName(self.currentClient)),
                ('Street name:        {}'.format(self.currentClient.GetStreetname()), lambda: self.clientView.inputStreetName(self.currentClient)),
                ('House number:       {}'.format(self.currentClient.GetHousenumber()), lambda: self.clientView.inputHouseNumber(self.currentClient)),
                ('Zipcode:            {}'.format(self.currentClient.GetZipcode()), lambda: self.clientView.inputZipCode(self.currentClient)),
                ('City:               {}'.format(self.currentClient.GetCity()), lambda: self.addCity()),
                ('Email address:      {}'.format(self.currentClient.GetEmail()), lambda: self.clientView.inputEmail(self.currentClient)),
                ('Phone number:       {}'.format(self.currentClient.GetPhone()), lambda: self.clientView.inputPhone(self.currentClient)),
                ('CONFIRM', lambda: self.confirmNewClient()),
                ('RETURN', self.skip)
            ]
            exit = self.switchfunctionInput(options, [10])
            if exit == True:
                return

    def confirmNewClient(self):
        if self.clientController.Save(self.currentClient) == True:
            self.mainMenu()
        else:
            self.registerNewClient()


        
    def registerNewUser(self, role):
        self.currentUser = User()
        while True:
            if role == 'advisor':
                print('-----------------[ Register new Advisor ]-----------------\n')
            elif role == 'admin':
                print('------------------[ Register new Admin ]------------------\n')
            print(' Choose the option of the value you want to change, then choose confirm to save\n')
            options = [
                (f'Username:         {self.currentUser.GetUsername()}', lambda: self.userView.inputUsername(self.currentUser)),
                (f'Password:         {self.currentUser.GetPassword()}', lambda: self.userView.inputPassword(self.currentUser)),
                (f'First name:       {self.currentUser.GetFname()}', lambda: self.userView.inputFname(self.currentUser)),
                (f'Last name:        {self.currentUser.GetLname()}', lambda: self.userView.inputLname(self.currentUser)),
                ('CONFIRM', lambda: self.confirmNewUser(role)),
                ('RETURN', self.skip)
            ]
            exit = self.switchfunctionInput(options, [6])
            if exit == True:
                return

    def confirmNewUser(self, role):
        if self.userController.Save(self.currentUser, role) == True:
            self.mainMenu()
        else:
            self.registerNewUser(role)

    def modifyUser(self, user):
        self.currentUser = user
        while True:
            if user.role == 'advisor':
                print('--------Modify advisor--------')
            elif user.role == 'admin':
                print('-----Modify administrator-----')
            options = [
                (f'Username:         {self.currentUser.GetUsername()}', lambda: self.userView.inputUsername(user)),
                (f'First name:       {self.currentUser.GetFname()}', lambda: self.userView.inputFname(user)),
                (f'Last name:        {self.currentUser.GetLname()}', lambda: self.userView.inputLname(user)),
                (f'Reset to temporary password', lambda: self.userController.SetTempPassword(user)),
                ('Confirm changes', lambda: self.confirmModifyUser(user)),
                ('Delete user', lambda: self.confirmDeleteUser(user)),
                ('Return to search', self.skip)
            ]
            exit = self.switchfunctionInput(options, [7])
            if exit == True:
                return

    def confirmDeleteUser(self, user):
        if self.accountController.Remove(user) == True:
            self.mainMenu()
        else:
            self.modifyUser(user)

    def confirmModifyUser(self, user):
        if self.userController.UpdateUser(user) == True:
            self.mainMenu()
        else:
            self.modifyUser(user)

    def modifyClient(self, client):
        while True:
            print('-----Modify client-----')
            options = [
                ('First name:        {}'.format(client.GetFname()), lambda: self.clientView.inputFirstName(client)),
                ('Last name:         {}'.format(client.lastname), lambda: self.clientView.inputLastName(client)),
                ('Street name:       {}'.format(client.GetStreetname()), lambda: self.clientView.inputStreetName(client)),
                ('House number:      {}'.format(client.GetHousenumber()), lambda: self.clientView.inputHouseNumber(client)),
                ('Zipcode:           {}'.format(client.GetZipcode()), lambda: self.clientView.inputZipCode(client)),
                ('City:              {}'.format(client.GetCity()), lambda: self.addCity()),
                ('Email address:     {}'.format(client.email), lambda: self.clientView.inputEmail(client)),
                ('Phone number:      {}'.format(client.phone), lambda: self.clientView.inputPhone(client)),
                ('Confirm changes', lambda: self.clientController.Save(self.currentClient)), #TODO return to main menu?
                ('Delete client', lambda: self.confirmDeleteClient(client)),
                ('RETURN', self.skip)
            ]
            exit = self.switchfunctionInput(options, [11])
            if exit == True:
                return

    def confirmDeleteClient(self, client):
        if self.clientController.Remove(client) == True:
            self.mainMenu()
        else:
            self.modifyClient(client)

    def confirmModifyClient(self, client):
        if self.clientController.Save(client) == True:
            self.mainMenu()
        else:
            self.modifyClient(client)

    def addCity(self):
        while True:
            print('\n -------------------------[ City ]-------------------------\n')
            options = [
                (" New York", lambda: self.currentClient.SetCity("New York")),
                (" Tokyo", lambda: self.currentClient.SetCity("Tokyo")),
                (" London", lambda: self.currentClient.SetCity("London")),
                (" Paris", lambda: self.currentClient.SetCity("Paris")),
                (" Sydney", lambda: self.currentClient.SetCity("Sydney")),
                (" Signapore", lambda: self.currentClient.SetCity("Signapore")),
                (" Los Angeles", lambda: self.currentClient.SetCity("Los Angeles")),
                (" Toronto", lambda: self.currentClient.SetCity("Toronto")),
                (" Amsterdam", lambda: self.currentClient.SetCity("Amsterdam")),
                ("San Jose", lambda: self.currentClient.SetCity("San Jose"))
            ]
            options.append(('RETURN', self.skip))
            exit = self.switchfunctionInput(options, [11])
            if exit == True:
                return

    def SearchUserByName(self, role):
        while True:
            print("\n Please enter name to search for or type 'exit' to leave\n")
            userinput = input(" Name: ")
            if userinput == 'exit':
                return
            users = self.userController.GetUserByName(userinput, role)
            if len(users) != 0:
                self.userListMenu(users)
                return
            else:
                print('\n ERROR: No users containing this name found, please try again.')

    def SearchUserByUsername(self, role):
        while True:
            print("\n Please enter name to search for or type 'exit' to leave\n")
            userinput = input(" Username: ")
            if userinput == 'exit':
                return
            users = self.userController.GetUserByUsername(userinput, role)
            if len(users) != 0:
                self.userListMenu(users)
                return
            else:
                print('\n ERROR: No users containing this username found, please try again.')

    def ShowAllUsers(self, role):
        while True:
            #print("\n Please enter name to search for or type 'exit' to leave\n")
            #userinput = input(" Username: ")
            #if userinput == 'exit':
            #    return
            users = self.userController.GetAllUsers(role)
            if len(users) != 0:
                self.userListMenu(users)
                return
            else:
                print('\n ERROR: No users found, please try again.')

    def SearchClientByName(self):
        while True:
            print("\n Please enter name to search for or type 'exit' to leave\n")
            userinput = input(" Name: ")
            if userinput == 'exit':
                return
            clients = self.clientController.GetClientByName(userinput)
            if len(clients) != 0:
                self.clientListMenu(clients)
                return
            else:
                print('\n ERROR: No clients containing this name found, please try again.')
            
    def SearchClientByEmail(self):
        while True:
            print("\n Please enter email to search for or type 'exit' to leave\n")
            userinput = input(" Email: ")
            if userinput == 'exit':
                return
            clients = self.clientController.GetClientByEmail(userinput)
            if len(clients) != 0:
                self.clientListMenu(clients)
                return
            else:
                print('\n ERROR: No clients containing this email found, please try again.')

    def ShowClients(self):
        while True:
            #print("\n Please enter name to search for or type 'exit' to leave\n")
            #userinput = input(" Name: ")
            #if userinput == 'exit':
            #    return
            clients = self.clientController.GetAllClients()
            if len(clients) != 0:
                self.clientListMenu(clients)
                return
            else:
                print('\n ERROR: No clients found, please try again.')

    #TODO layout verbeteren
    def userListMenu(self, users):
        print('\n----------------[ Advisors List ]----------------')
        print(f"{'      ID'}| {'Username':15}| {'First name':15}| {'Last name':15}| {'Registration date'}")
        options = []
        for u in users:
            options.append(((f'{u.id:4}| {u.username:15}| {u.firstname:15}| {u.lastname:15}| {u.registrationDate}'), lambda u=u: self.modifyUser(u)))
        options.append(('RETURN', self.skip))
        self.switchfunction(options)

    #TODO layout verbeteren
    def clientListMenu(self, clients):
        print('\n----------------[ Client List ]----------------')
        print(f"{'      ID'}| {'First name':15}| {'Last name':15}| {'Address':30}| {'Email':25}| {'Phone'}")
        options = []
        for c in clients:
            address = f'{c.streetname} {c.housenumber}'
            options.append(((f'{c.id:4}| {c.firstname:15}| {c.lastname:15}| {address:30}| {c.email:25}| {c.phone}'), lambda c=c: self.modifyClient(c)))
        options.append(('RETURN', self.skip))
        self.switchfunction(options)
        

    def switchfunctionInput(self, options, returnoptions):
        counter = 1
        for o in options:
            print(' {}. {}'.format(counter, o[0]))
            counter += 1
        userinput = input("\n Option: ")
        if(self.validator.inputNumberIsInRange(userinput, 1, len(options))):
            func = options[int(userinput) - 1][1]
            func()
            if(int(userinput) in returnoptions):
                return True

    def placeHolder(self):
        print('ERROR: If you see this the method is not finished yet.')

    def skip(self):
        return
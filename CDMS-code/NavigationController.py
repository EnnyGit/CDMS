import ValidationController as validation

class Navigator:
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
            ('Register new client', self.placeHolder),
            ('Update own password', self.placeHolder),
            ('Search advisors', self.searchAdvisor),
        ]

        if True: #TODO replace with access rights check
            options.append(('Register new advisor', self.placeHolder))
            options.append(('Administration menu', self.administrationMenu))
        if True:  #TODO replace with access rights check
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

    def placeHolder(self):
        print('If you see this the method is not finished yet.')

    def skip(self):
        return
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

    def mainMenu(self):
        options = [
            ('Search client', self.searchClient),
            ('Register new client', self.placeHolder),
            ('Update own password', self.placeHolder),
            ('Search advisors', self.placeHolder),
        ]

        if True: #TODO replace with access rights check
            options.append(('Register new advisor', self.placeHolder))
            options.append(('Administration menu', self.placeHolder))
        if True:  #TODO replace with access rights check
            options.append(('Register new system adminitrator', self.placeHolder))
            options.append(('Search administrators', self.placeHolder))

        options.append(('Exit', exit))

        self.switchfunction(options)

    def searchClient(self):
        #TODO Implement method
        return

    def placeHolder(self):
        print('If you see this the method is not finished yet.')

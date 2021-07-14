from AddressModel import Address

class Client:
    def __init__(self) -> None:
        self.fullname = ''
        self.address = None
        self.email = ''
        self.phone = None

    #TODO Input validation
    def setName(self):
        self.fullname = input('Please input clients full name\n')

    #TODO Input validation
    def setEmail(self):
        self.email = input('Please input clients email\n')

    #TODO Input validation
    def setPhone(self):
        self.phone = input('Please input clients phone\n')

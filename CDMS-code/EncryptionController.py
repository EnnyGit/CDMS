class EncryptionController:
    allowedcharacters = '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/'''
    offset = 5

    def __init__(self):
        pass

    def CaesarCipher(self, input):
        encryptedstring = ''
        for character in input:
            currentposition = self.allowedcharacters.find(character)
            if (currentposition + self.offset) >= len(self.allowedcharacters):
                newposition = (currentposition + self.offset) % len(self.allowedcharacters)
            else:
                newposition = currentposition + self.offset
            encryptedstring += self.allowedcharacters[newposition]
        return encryptedstring

    def CaesarDecipher(self, encryptedstring):
        decryptedstring = ''
        for character in encryptedstring:
            currentposition = self.allowedcharacters.find(character)
            if (currentposition - self.offset) < 0:
                newposition = len(self.allowedcharacters) + (currentposition - self.offset)
            else:
                newposition = currentposition - self.offset
            decryptedstring += self.allowedcharacters[newposition]
        return decryptedstring
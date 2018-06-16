import string

from collections import OrderedDict
from ciphers import Cipher

class Keyword(Cipher):
    
    def __init__(self):
        self.plaintext = [char for char in string.ascii_uppercase]
        self.encoded = [char for char in string.ascii_uppercase]
    
                
    def encrypt(self, text, keyword):
        self.text = text.upper()
        self.keyword = [char.upper() for char in keyword]      
        self.keyword = list(OrderedDict.fromkeys(self.keyword))
        for letter in self.keyword:
            self.encoded.remove(letter)
        for letter in reversed(self.keyword):
            self.encoded.insert(0, letter)
        mapping = {decode: encode for decode, encode in zip(self.plaintext, self.encoded)}
        encrypted =''
        for letter in self.text:
            try:
                encrypted += mapping[letter]
            except KeyError:
                encrypted += letter
        print("Encrypted this is: {}".format(encrypted))

    def decrypt(self, text, keyword):
        self.text = text.upper()
        self.keyword = [char.upper() for char in keyword]      
        self.keyword = list(OrderedDict.fromkeys(self.keyword))
        for letter in self.keyword:
            self.encoded.remove(letter)
        for letter in reversed(self.keyword):
            self.encoded.insert(0, letter)
        mapping = {decode: encode for decode, encode in zip(self.encoded, self.plaintext)}
        print(mapping)
        decrypted =''
        for letter in self.text:
            try:
                decrypted += mapping[letter]
            except KeyError:
                decrypted += letter
        print("Encrypted this is: {}".format(decrypted))
        
x = Keyword()
x.encrypt('Secret messages are great', 'Treehouse')
x.decrypt('NOEMOP GONNTSON TMO SMOTP', 'Treehouse')

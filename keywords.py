import string
from collections import OrderedDict
from ciphers import Cipher


class Keyword(Cipher):
    """
    Implements the behaviour of a Keyword cipher.
    """

    def __init__(self):
        self.plaintext = [char for char in string.ascii_uppercase]
        self.encoded = [char for char in string.ascii_uppercase]

    def encrypt(self, text, keyword):
        """
        Encrypts text using the logic of a Keyword cipher.
        Takes a text and a keyword argument.
        Returns the encrypted text.
        """
        self.text = text.upper()
        self.keyword = [char.upper() for char in keyword]
        self.keyword = list(OrderedDict.fromkeys(self.keyword))
        for letter in self.keyword:
            self.encoded.remove(letter)
        for letter in reversed(self.keyword):
            self.encoded.insert(0, letter)
        mapping = {decode: encode for decode,
                   encode in zip(self.plaintext, self.encoded)}
        encrypted = ''
        for letter in self.text:
            try:
                encrypted += mapping[letter]
            except KeyError:
                encrypted += letter
        return encrypted

    def decrypt(self, text, keyword):
        """
        Decrypts text encrypted using a Keyword cipher.
        Takes an encrypted text and a keyword argument.
        Returns the decrypted text.
        """
        self.text = text.upper()
        self.keyword = [char.upper() for char in keyword]
        self.keyword = list(OrderedDict.fromkeys(self.keyword))
        for letter in self.keyword:
            self.encoded.remove(letter)
        for letter in reversed(self.keyword):
            self.encoded.insert(0, letter)
        mapping = {decode: encode for decode,
                   encode in zip(self.encoded, self.plaintext)}
        decrypted = ''
        for letter in self.text:
            try:
                decrypted += mapping[letter]
            except KeyError:
                decrypted += letter
        return decrypted

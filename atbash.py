import string
from ciphers import Cipher


class Atbash(Cipher):
    """
    Implements the behaviour of an Atbash cipher.
    """
    def __init__(self):
        self.plaintext = {key: value for key, value
                          in zip(string.ascii_uppercase,
                                 string.ascii_uppercase[::-1])}
        self.plaintext_rev = {key: value for key, value
                              in zip(string.ascii_uppercase[::-1],
                                     string.ascii_uppercase)}
        self.plaintext[' '] = ' '
        self.plaintext_rev[' '] = ' '

    def encrypt(self, text):
        """
        Encrypts text using the logic of an Atbash cipher.
        Returns the encrypted text.
        """
        self.text = text.upper()
        encoded = ''
        for x in self.text:
            try:
                encoded += self.plaintext[x]
            except IndexError:
                encoded += x
        return encoded

    def decrypt(self, text):
        """
        Decrypts text that has been encrypted with an Atbash cipher.
        Returns the decrypted text.
        """
        self.text = text.upper()
        decoded = ''
        for x in self.text:
            try:
                decoded += self.plaintext_rev[x]
            except IndexError:
                decoded += x
        return decoded
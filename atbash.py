import string
from ciphers import Cipher


class Atbash(Cipher):

    def __init__(self):
        self.plaintext = {key: value for key, value
                          in zip(string.ascii_uppercase,
                                 string.ascii_uppercase[::-1])}
        self.plaintext_rev = {key: value for key, value
                              in zip(string.ascii_uppercase[::-1],
                                     string.ascii_uppercase)}
        print(self.plaintext)

    def encrypt(self, text):
        """
        Encrypts text using the Atbash cipher.
        Returns encrypted text.
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
        Decrypts text that has been encrypted with the Atbash cipher.
        Returns decrypted text.
        """
        self.text = text.upper()
        decoded = ''
        for x in self.text:
            try:
                decoded += self.plaintext_rev[x]
            except IndexError:
                decoded += x
        return decoded

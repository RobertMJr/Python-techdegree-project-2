import string
from ciphers import Cipher


class Affine(Cipher):

    def __init__(self):
        self.plaintext = {key: value for key,
                          value in zip(string.ascii_uppercase, range(0, 26))}
        self.plaintext_rev = {key: value for key,
                              value in zip(range(0, 26),
                                           string.ascii_uppercase)}
        self.modular_inverse = {1: 1,
                                3: 9,
                                5: 21,
                                7: 15,
                                9: 3,
                                11: 19,
                                15: 7,
                                17: 23,
                                19: 11,
                                21: 5,
                                23: 7,
                                25: 25}

    def encrypt(self, text, a_key, b_key):
        """
        Encrypts text using the affine cipher,
        two numeric keys are required,
        first key must be coprime with 26.

        Returns the encrypted text
        """
        self.text = text.upper()
        self.a_key = a_key
        self.b_key = b_key
        encoded = []
        encrypted = ''
        for x in self.text:
            try:
                val = self.plaintext[x]*self.a_key+self.b_key
                encoded.append(val % 26)
            except KeyError:
                encoded.append(x)
        for x in encoded:
            try:
                encrypted += self.plaintext_rev[x]
            except KeyError:
                encrypted += x
        return encrypted

    def decrypt(self, text, a_key, b_key):
        """
        Decrypts text encrypted with the affine cipher,
        two numeric keys are required,
        same keys used for encrypting.

        Returns the decrypted text
        """
        self.text = text.upper()
        self.a_key = self.modular_inverse[a_key]
        self.b_key = b_key
        decoded = []
        decrypted = ''
        for x in self.text:
            try:
                val = self.a_key*(self.plaintext[x] - self.b_key)
                decoded.append(val % 26)
            except KeyError:
                decoded.append(x)
        for x in decoded:
            try:
                decrypted += self.plaintext_rev[x]
            except KeyError:
                decrypted += x
        return decrypted


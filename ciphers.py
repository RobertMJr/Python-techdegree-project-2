import string
import random
from string import digits, punctuation


class Cipher:

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    def one_time_pad(self, text, pad, encrypt=True):
        """
        Implements a one time pad
       """
        self.alfabet = {key: value for key, value
                        in zip(string.ascii_uppercase, range(0, 26))}
        self.alfabet_rev = {key: value for key, value
                            in zip(range(0, 26), string.ascii_uppercase)}
        self.text = text.upper()
        self.pad = pad.upper()
        self.text_code = []
        self.enco = ''
        if len(self.text) > len(self.pad):
            missing = len(self.text) - len(self.pad)
            for i in range(missing):
                self.pad += self.pad[i]
        elif len(self.text) < len(self.pad):
            limit = len(self.text)
            self.pad = self.pad[:limit]
        if encrypt:
            for x, y in zip(self.text, self.pad):
                try:
                    val = self.alfabet[x] + self.alfabet[y]
                    self.text_code.append(val % 26)
                except KeyError:
                    # make sure self.pad has no spaces
                    self.text_code.append(x)
            for x in self.text_code:
                try:
                    self.enco += self.alfabet_rev[x]
                except KeyError:
                    self.enco += x
        else:
            for x, y in zip(self.text, self.pad):
                try:
                    val = self.alfabet[x] - self.alfabet[y]
                    self.text_code.append(val % 26)
                except KeyError:
                    self.text_code.append(x)
            for x in self.text_code:
                try:
                    self.enco += self.alfabet_rev[x]
                except KeyError:
                    self.enco += x

        return self.enco

    def add_padding(self, text):
        """
        Adds padding to the text.
        Returns text in blocks of 5 characters
        """
        print('You are here')
        self.text = text
        special = list(digits)
        special_c = list(punctuation)
        five_block = ''
        list_of_words = []
        for i in text:
                if len(five_block) < 5:
                        five_block += i
                else:
                    list_of_words.append(five_block)
                    five_block = ''
                    five_block += i
        list_of_words.append(five_block)
        for x, i in enumerate(list_of_words):
            if len(i) < 5:
                size = 5-len(i)
                i += ''.join(random.choices(special, k=size))
                list_of_words[x] = i
            else:
                list_of_words[x] = i.replace(" ", random.choice(punctuation))
        return ' '.join(list_of_words).upper()

    def remove_padding(self, text):
        """
        Removes padding from text
        Returns text without the added padding
        """
        self.text = text
        special = list(digits)
        special_c = list(punctuation)
        words = ''
        for i in text:
            if i.isalpha():
                    words += i
            elif i in special_c:
                    words += i.replace(i, ' ')
            elif i in special:
                    pass
        return words.upper()


import os
import string
from ciphers import Cipher
from caesar import Caesar
from keywords import Keyword
from affine import Affine
from atbash import Atbash

working = True


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


letters = string.ascii_uppercase
stripped_text = ''

while working:
    clear_screen()
    print("This is the Secret Messages project for the Treehouse Techdegree. \n"
          " These are the current available ciphers: \n"
          "- Affine \n"
          "- Atbash \n" 
          "- Caesar \n"
          "- Keyword \n"
          "- Press (Q) to quit.")
    choice = input("Which cipher would you like to use? \n")
    if choice.upper() == 'Q':
        break
    elif (choice.upper() == 'AFFINE' or choice.upper() == 'ATBASH' or choice.upper() == 'CAESAR' or
            choice.upper() == 'KEYWORD'):
        print('Excellent choice. \n')
        text_choice = input('What is your message? (Please note that punctuation and digits will be removed) \n')
        for i in text_choice:
            if i.upper() not in letters and i != ' ':
                pass
            else:
                stripped_text += i
        text_choice = stripped_text
        print(text_choice)
        break

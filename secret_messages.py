import os
import string
from ciphers import Cipher
from caesar import Caesar
from keywords import Keyword
from affine import Affine
from atbash import Atbash

working = True
cipher_choice = True
letters = string.ascii_uppercase


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def strip_non_letters(txt):
    stripped_text = ''
    for i in txt:
        if i.upper() not in letters and i != ' ':
            pass
        else:
            stripped_text += i
    txt = stripped_text
    return txt


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
    elif choice.upper == 'AFFINE':
        cipher = Affine()
    elif choice.upper() == 'ATBASH':
        cipher = Atbash()
    elif choice.upper() == 'CAESAR':
        cipher = Caesar()
    elif choice.upper() == 'KEYWORD':
        cipher = Keyword()
    else:
        print('Sorry, that is not a valid choice. Try again. \n')




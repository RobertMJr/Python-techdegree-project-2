import os
import string
from ciphers import Cipher
from caesar import Caesar
from keywords import Keyword
from affine import Affine
from atbash import Atbash

working = True
cipher_choice = True
enc_dec = True
letters = string.ascii_uppercase


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



while working:
    clear_screen()
    print("This is the Secret Messages project for the Treehouse Techdegree. \n"
          " These are the current available ciphers: \n"
          "- Affine \n"
          "- Atbash \n" 
          "- Caesar \n"
          "- Keyword \n"
          "- Press (Q) to quit.")
    while cipher_choice:
        choice = input("Which cipher would you like to use? \n")
        if choice.upper() == 'Q':
            exit()
        elif choice.upper() == 'AFFINE':
            cipher = Affine()
            break
        elif choice.upper() == 'ATBASH':
            cipher = Atbash()
            break
        elif choice.upper() == 'CAESAR':
            cipher = Caesar()
            break
        elif choice.upper() == 'KEYWORD':
            cipher = Keyword()
            break
        else:
            print('Type the name of any available cipher. \n')

    user_text = input('What is your message? \n'
                      'NOTE: Use letters only. \n')

    while enc_dec:
        e_or_d = input('Are we going to encrypt or decrypt? \n')
        if e_or_d.upper() == 'ENCRYPT' and isinstance(cipher, Affine):
            alpha_key = input('Choose the first key,  must be a number that'
                              ' is coprime with the number twenty six (26). \n')
            alpha_key = int(alpha_key)
            magnitude = input('Chose the magnitude key, must be a number. \n')
            magnitude = int(magnitude)
            ot_pad  = input('Type your one time pad. \n')
            ot_val = cipher.one_time_pad(user_text, ot_pad)
            value = cipher.encrypt(ot_val,alpha_key, magnitude)
            block_choice = input('Do you want the output to be displayed in blocks of 5? (Y/N) \n')
            if block_choice.upper() == 'Y':
                value = cipher.add_padding(value)
                print(value + '\n')
                break
            else:
                print(value + '\n')
                break
        elif e_or_d.upper() == 'DECRYPT' and isinstance(cipher, Affine):
            alpha_key = input('Type in the first key that was used,  must be a number that'
                              ' is coprime with the number twenty six (26). \n')
            alpha_key = int(alpha_key)
            magnitude = input('Type in the magnitude key that was used, must be a number. \n')
            magnitude = int(magnitude)
            ot_pad  = input('Type your one time pad, must be the same used for encrypting. \n')
            no_block = cipher.remove_padding(user_text)
            value = cipher.decrypt(no_block, alpha_key, magnitude)
            ot_val = cipher.one_time_pad(value, ot_pad, encrypt=False)
            print(ot_val + '\n')
            break
        elif e_or_d.upper() == 'ENCRYPT' and isinstance(cipher, Atbash):
            ot_pad = input('Type your one time pad. \n')
            ot_val = cipher.one_time_pad(user_text, ot_pad)
            value = cipher.encrypt(ot_val)
            block_choice = input('Was the output displayed in blocks of 5? (Y/N) \n')
            if block_choice.upper() == 'Y':
                value = cipher.add_padding(value)
                print(value)
                break
            else:
                print(value)
                break
        elif e_or_d.upper() == 'DECRYPT' and isinstance(cipher, Atbash):
            ot_pad = input('Type your one time pad, must be the same used for encrypting. \n')
            no_block = cipher.remove_padding(user_text)
            value = cipher.decrypt(no_block)
            ot_val = cipher.one_time_pad(value, ot_pad, encrypt=False)
            print(ot_val)
            break
        else:
            ('Type "encrypt" or "decrypt". \n')

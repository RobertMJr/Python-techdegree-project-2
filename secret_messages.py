import os
from ciphers import Cipher
from caesar import Caesar
from keywords import Keyword


def clear_screen():
    os.system('cls' if os.name =='nt' else 'clear')

print("This is the Secret Messages project for the Treehouse Techdegree. \n"
      "These are the current available ciphers: \n"
      "- Caesar \n"
      "- Keyword \n")
choice = input("Which cipher would you like to use? ")
if choice == "Caesar" or choice == "Keyword":
    message = input("That's an excelent cipher. What's the message? ")
else:
    raise ValueError("That cipher is not implemented.")
encrypt_or_decrypt = input("Are we going to encrypt or decrypt? ")


    

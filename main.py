from sqlite3 import apilevel


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
direction = input("To encrypt chose encode to decrypt chose decode: \n")
text = input("Enter a text to encode: \n")
shift = int(input("Enter a number to shift: \n"))


def encrypt(plain_text, shift_amount):
    encoded_word = ''
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position + shift
        encoded_word += alphabet[new_position]
    print(f"Your encode word is {encoded_word}")


encrypt(plain_text=text, shift_amount=shift)
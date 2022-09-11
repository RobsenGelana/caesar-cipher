from sqlite3 import apilevel


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
direction = input("To encrypt chose encode to decrypt chose decode: \n").lower()
text = input("Enter a text to encode: \n").lower()
shift = int(input("Enter a number to shift: \n"))


def encrypt(plain_text, shift_amount):
    encoded_word = ''
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position + shift
        encoded_word += alphabet[new_position]
    print(f"Your encode word is {encoded_word}")


def decrypt(plain_text, shift_amount):
    decoded_word = ''
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position - shift
        decoded_word += alphabet[new_position]
    print(f"The decoded word is {decoded_word}")

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(plain_text=text, shift_amount=shift)
else:
    print("Invalid input")
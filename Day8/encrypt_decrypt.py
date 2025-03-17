# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#              'v',
#              'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
#              'R',
#              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ' ']
#
#
# def encrypt(ip_word, position):
#     global encrypted_word
#     encrypted_word = ''
#     for letter in ip_word:
#         shifted_pos = alphabets.index(letter) + position
#         # print(shifted_pos)
#         if shifted_pos < int(52):
#             encrypted_word = encrypted_word + alphabets[shifted_pos]
#             # print("Your encrypted LETTER is:", encrypted_word)
#         else:
#             shifted_pos = shifted_pos - 52
#             print(shifted_pos)
#             encrypted_word = encrypted_word + alphabets[shifted_pos]
#             # print("Your encrypted LETTER is:", encrypted_word)
#             # print("Error")
#     print("Your encrypted word is:", encrypted_word)
#
#
# def decrypt(output_word, position):
#     decrypted_word = ''
#     for letter in output_word:
#         shifted_pos = alphabets.index(letter) - position
#         if shifted_pos < int(52):
#             decrypted_word = decrypted_word + alphabets[shifted_pos]
#             # print("Your encrypted LETTER is:", encrypted_word)
#         else:
#             shifted_pos = shifted_pos - 52
#             print(shifted_pos)
#             encrypted_word = encrypted_word + alphabets[shifted_pos]
#     print("Your decrypted word is:", decrypted_word)
#
# original_text = input("Type the word you want to encrypt: ")
# shift_amount = int(input("Type the shift amount: "))
# encrypt(ip_word=original_text, position=shift_amount)
# decrypt(output_word=encrypted_word, position=shift_amount)


alphabets = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")


def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter in alphabets:
            new_pos = (alphabets.index(letter) + shift) % 52
            encrypted_text += alphabets[new_pos]
        else:
            encrypted_text += letter  # Keep non-alphabet characters unchanged
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)  # Reuse encrypt function for decryption


# User Input
original_text = input("Type the word you want to encrypt: ")
shift_amount = int(input("Type the shift amount: "))

# Encrypt & Decrypt
encrypted_text = encrypt(original_text, shift_amount)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift_amount)
print("Decrypted:", decrypted_text)

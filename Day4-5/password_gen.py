import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# len_of_pass = int(input("Length Of the password? "))
num_letters = int(input("How many min letters do you want? "))
num_numbers = int(input("How many min digits do you want? "))
num_symbols = int(input("How many min symbols do you want? "))

count = 0
pass_word = ''

for a_letter in range(1, num_letters + 1):
    pass_word = (pass_word + random.choice(letters))
# print(pass_word)

for a_number in range(1, num_numbers + 1):
    pass_word = (pass_word + random.choice(numbers))
# print(pass_word)

for a_symbol in range(1, num_symbols + 1):
    pass_word = (pass_word + random.choice(symbols))

#sequence
print(pass_word)


# #randomized

password_list = []

for a_letter in range(1, num_letters + 1):
    password_list.append(random.choice(letters))

for a_number in range(1, num_numbers + 1):
    password_list.append(random.choice(numbers))

for a_symbol in range(1, num_symbols + 1):
    password_list.append(random.choice(symbols))

#sequence
print(password_list)
random.shuffle(password_list)
password = ''

for char in password_list:
    password += char

print("Password: ", password)






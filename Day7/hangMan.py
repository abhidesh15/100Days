#Randomly chose a letter from word_list
import random

print("Hi! Lets play hangman!\n\n")

word_list = ["Cherry", "Guava", "Pineapple", "Mango", "Orange"]
random_word = random.choice(word_list)
print("Your word is a:")
print(random_word)

max_chances = int(10)
win_chance = 0
count = 1
dash_list = []

while count <= len(random_word):
    dash_list.append("_")
    count += 1

word = ''
for letter in dash_list:
    word = word + letter
    # word = word + letter

while max_chances > 0:
    guess_letter = input("Guess a letter? ").lower()
    if guess_letter in random_word:
        print("You guessed it right!")
        win_chance += 1
        if win_chance == len(random_word):
            print("Congrats, You Win! The Word is:", random_word)
            exit(0)
    else:
        print("You guessed it wrong")
        max_chances -= 1
        if max_chances == 0:
            print("Sorry, You Lost!")
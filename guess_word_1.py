import random

name = input("What is your name? ")

print("All the best", name, "!")

words = ["copy", "book", "pencil", "eraser", "computer", "planets"]

word = random.choice(words)
print(word)
length = len(word)

for letter in word:
    print("_")

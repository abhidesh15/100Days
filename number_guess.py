import random
import math
lower = int(input("Enter Lower bound:- "))

upper = int(input("Enter Upper bound:- "))
chance = int(0)

while lower > upper:
    chance += 1

    if chance > 3:
        print("Sorry!"
              "You've exceeded the number of chances to select the range."
              "Exiting the game now.")
        exit()

    print("Guess a number greater than the lower number i.e.:", lower)
    upper = int(input("Enter Upper bound:- "))

x = random.randint(lower, upper)
#print("Random Number:", x)


num = int(0)
tries = int(0)

while num != x:
    num = int(input("Guess the number:"))
    tries = tries + 1
    if num < x:
        print("You guessed a number lower than the actual. Try Again!")
    elif num > x:
        print("You guessed a number greater than the actual. Try Again!")
    else:
        print("You guessed it right! Congratulations!")
        print("You took " + str(tries) + " chance/s to guess it right!")



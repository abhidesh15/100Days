import random

print(" ---------------------------------\n|  Lets Play Rock Paper Scissors  |\n ---------------------------------\n")

while True:
    choice = int(input("Type 0 for rock, 1 for paper or 2 for scissors: \n"))

    if choice == 0 or choice == 1 or choice == 2:

        comp_choice = random.randint(0, 2)
        print("Computer's Choice is:", comp_choice, "\n")

        if (choice == 0 and comp_choice == 1) or (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 0):
            print("You Lose! :( ")
        elif (choice == 1 and comp_choice == 0) or (choice == 2 and comp_choice == 1) or (choice == 0 and comp_choice == 2):
            print("You Win! :D")
        elif (choice == 0 and comp_choice == 0) or (choice == 1 and comp_choice == 1) or (choice == 2 and comp_choice == 2):
            print("Its a tie!")
    else:
        print("Incorrect input!")

    play_again = input("Play again? Y or N: ").upper()
    print("\n")

    if play_again == 'N':
        print("Thank you for playing!")
        exit()


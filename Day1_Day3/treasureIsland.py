print("Welcome to treasure island! Let us begin.")

left_right = input("Choose Left or Right? L or R")
if left_right == 'L':
    swim_wait = input("Choose swim or wait? S or W")
    if swim_wait == 'W':
        door = input("Choose 1 door! Red, Blue, Yellow. R, B, Y")
        if door == 'Y':
            print("Congratulations! You Win!")
        elif door == 'R':
            print("Burned By Fire!\n   Game Over!   ")
        elif door == 'B':
            print("Eaten by beasts!\n   Game Over!")
        else:
            print("Your option not available!\n     Game Over!")
    elif swim_wait == 'S':
        print("Attached by trout.\n    Game Over")
    else:
        print("Your option not available!\n     Game Over!")
elif left_right == 'R':
    print("Fall in a hole!\n   Game Over!")
else:
    print("Your option not available!\n     Game Over!")


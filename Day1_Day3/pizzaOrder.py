print("Welcome to Pizza Delivery!")


pepperoni_small = 2
pepperoni_medium_large = 3
extra_cheese_any_size = 1

while True:
    size = input("What size pizza do you want? S, M or L: ")
    pepperoni = input("Do you want pepperoni? Y or N: ")
    extra_cheese = input("Do you want extra cheese? Y or N: ")

    if size.upper() == 'S':
        price = 15
        break
    elif size.upper() == 'M':
        price = 20
        break
    elif size.upper() == 'L':
        price = 25
        break
    else:
        print("You typed a wrong input. Please try again.")
        continue

if pepperoni.upper() == 'Y' and extra_cheese.upper() == 'Y':
    price = price + pepperoni_small + extra_cheese_any_size
elif pepperoni.upper() == 'Y' and extra_cheese.upper() == 'N':
    price = price + pepperoni_small
elif pepperoni.upper() == 'N' and extra_cheese.upper() == 'Y':
    price = price + extra_cheese_any_size

print(f"Your total amount is: {price}")



def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


while True:
    a = int(input("Enter a number: "))
    b = int(input("Enter 2nd number: "))
    operand = input("""
Enter anyone from following operations -
+
-
*
/
""")

    if operand == '+':
        print(add(a, b))
    elif operand == '-':
        print(subtract(a, b))
    elif operand == '*':
        print(multiply(a, b))
    else:
        print(divide(a, b))

    continue_operation = input("Do you want to continue? Press y or n: ")

    if continue_operation == 'Y' or continue_operation == 'y':
        continue
    else:
        exit()

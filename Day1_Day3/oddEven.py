# # If statement
# while True:
#     num = int(input("Type a number and I will tell if the number is odd or even: "))
#     # modulo = num % 2
#     if num % 2 == 0:
#         print(f"Your number - {num} is an even number!\n")
#     else:
#         print(f"Your number - {num} is an odd number!\n")
#
#     play_again = (input("Do you want to play again? type Y for yest or N for No: \n"))
#     if play_again == 'Y':
#         continue
#     else:
#         print("Thankyou for playing!")
#         exit()
#
# if-else statement

print("Welcome to the rollercoaster ride!")
age = int(input("Please enter your age: "))
height = int(input("Please enter your height in cm: "))

if (age < 4) or (age > 60):
    print("Sorry! You're not allowed to ride the rollercoaster!")
elif height < 100:
    print("Sorry! Your age is fine but you're too short to ride the rollercoaster.")
else:
    print("You can ride the rollercoaster!")


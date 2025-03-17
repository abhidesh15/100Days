name = input("What is you name? ")
print("Hello", name)
print("The length of your name is: ", len(name))
age = input("What is your age? ")
if int(age) < int(18):
    print("Sorry, your age is", age,".")
    print("We cannot allow you in the bar.")
else:
    print("Ok. You are",age,"years old.")
    print("You are allowed to come in.")



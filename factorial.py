import math

num = int(input("Enter the number: "))

print("Factorial of ", num, "is", math.factorial(num))

print("Taking factorial using conventional method.")
#count = num

for i in num:
    num = num*(num-1)
print(num)


while num != 1:
    num -= 1
    count = num * (num-1)
    print("Count -", count)
    print("Num -", num)

print("factorial using conventional method", count)

exit()

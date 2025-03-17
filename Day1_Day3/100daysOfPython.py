var = "Hello World"
print(var[2])

print(123_456_789 + 1)

# print("Hello" + str(len(input("Your name?"))))
print(5//3)
print(5/3)
print(5**3)

# Bill Calculator
print("Welcome to bil calculator!")
tot_bill = float(input("What was the total bill? "))
tip = int(input("How much tip do you want to give? "))
tot_ppl = int(input("How many ppl to split the bill? "))

pay = round(((tot_bill + (tip / 100 * tot_bill)) / tot_ppl), 2)
print(f"Each person bill: ${pay}")

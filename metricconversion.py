weight = input("What is your weight? ")
unit = input("Convert to Kg or Pounds? ")

if unit.upper() == 'kg':
    output = float(weight) * 0.45
    print("Weight in kgs: ", output)
else:
    output = float(weight) * 2.2
    print("Weight in Pounds: ", output)



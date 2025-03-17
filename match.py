x = int(input("Input an integer: "))

match x:
    case 5:
        print("Case is", x)
    case _ if x < 10:  # _ is used as default
        print("case is", x, " which is a single digit")
    case _ if 10 <= x < 100:
        print("Case is ", x, " which is a double digit")
    case _:
        print("Case is", x, "which is a three digit no")

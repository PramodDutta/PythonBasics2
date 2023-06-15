num = 10;
match num:
    case 0:
        print("Number is zero")
        # Perform actions for zero
    case x if x > 0:
        print("Number is positive")
        # Perform actions for positive number
    case x if x < 0:
        print("Number is negative")
        # Perform actions for negative number
    case _: #Default
        print("No Idea!!")


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
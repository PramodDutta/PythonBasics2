# Write a Program
# If user entered a +ve or -ve

num = int(input("Enter a int Number"))
print("You have entered a number -> ", str(num))

match num:
    case 0:
        print("You have entered 0")
    case num if num > 0:
        print("+ve Number")
    case num if num < 0:
        print("-ve Number")
    case _:
        print("No Idea!!")

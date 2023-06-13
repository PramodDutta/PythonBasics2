print("Start")

while True:
    user_input = input("Enter a Number, 0 to 10, If you match my number i will exit")
    print("You have written this number"+ user_input)
    user_input = int(user_input)
    if user_input == 5:
        print("You found the Lucky Number")
        break

print("End")

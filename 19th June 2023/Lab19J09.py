def num_if_50(num):
    if num > 50:
        print("Greater than 50")
    else:
        print("Less than 50")


# num_if_50(45)


r = lambda num: "Greater than 50" if num > 50 else "Lower than 50"
print(r(54))

# elif

user_input = int(input("Enter your Number"))
r2 = lambda x: x ** 2 if x > 0 else (x * 2 if x < 0 else 0)
print(r2(user_input)) # 3**2 -> 9

user_input = int(input("Enter your Number"))
print(r2(user_input)) # -2 * 2

user_input = int(input("Enter your Number"))
print(r2(user_input))  #0

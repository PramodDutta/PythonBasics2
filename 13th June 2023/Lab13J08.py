# String Formatting


name = input("Enter your name")
age = input("Enter you age")

print(f"Hello, {name}. You age is {age}")

print("Hello {} Your age is {}".format(name, age))

print("Hello %s, Your age is %s" % (name, age))

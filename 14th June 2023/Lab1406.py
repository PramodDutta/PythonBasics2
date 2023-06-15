password = input("Enter your Password")
#print(password.isnumeric())
#print(password.islower())
#print(password.isupper())
#print(password.isalpha()) # pramod ,abc , dutta, pie
# len < 6 - poor password

match password:
    case password if len(password) < 6:
        print("Too Short !! - Weak Password !!!!")
    case password if password.isnumeric():
        print("Weak Password, Numberic Only!!, Add Alpha")
    case password if password.islower():
        print("Weak Password, Lowercase Only!!, Add a Upper Char")
    case password if password.isupper():
        print("Weak Password, Uppercase Only!!, Add a Lower Case")
    case _:
        print("Strong Password!!")



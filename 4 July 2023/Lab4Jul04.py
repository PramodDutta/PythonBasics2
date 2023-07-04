# try:
#     # Open the file in read mode
#     file = open('pramod.txt', 'r')
#     # Read the contents of the file
#     contents = file.read()
#     print(contents)
# except FileNotFoundError:
#     print("File not found.")
# except IOError:
#     print("An error occurred while reading the file.")
# else:
#     print("File reading completed successfully.")


from PyPackage import Mod1 as p
print(p.sum(1,2))


import math
print(math.pow(2,3))


from PyPackage import Mod2
Mod2.greet("Pramod")

person = Mod2.Person("Amit")
person.intro()

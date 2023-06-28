# Encapsulation
# Data Members and Methods Together in a class

# Visibility
# Get and Set

# !! Public Member
# Public members have no special naming convention in Python and
# are accessible from anywhere.
# They can be accessed directly from outside the class and other modules.


# ----------------------
# !! Protected Member
# Protected members are denoted by a single underscore prefix (_).
# They can still be accessed from outside the class, but it is considered a
# best practice not to do so directly.


# ----------------------
# !! Private  Member
# Private members are denoted by a double underscore prefix (__).
# Private members are intended to be used within the class only.

class Myclass:
    def __init__(self):
        self.public_var = 10
        self._protected_var = 11
        self.__private_var = 12

    def public_method(self):
        print("This is Public Method")
        self.__private_method()
        print(self.__private_var)

    def _protected_method(self):
        print("This is Protected Method")
        self.__private_method()
        print(self.__private_var)

    def __private_method(self):
        print("This is a private method.")


obj = Myclass()
print(obj.public_var)
obj.public_method()


# print(obj._protected_var)
# obj._protected_method()

# obj.__private_var
#obj.__private_method()




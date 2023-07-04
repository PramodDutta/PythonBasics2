# Example 1: Division by zero exception
# try:
#     result = 10 / 0  # Attempting to divide by zero
# except ZeroDivisionError as error:
#     print("Error:", error)


# Example 1: Division by zero exception
try:
    x = int(input("Enter a Number!!"))
    result = 10 / x  # Attempting to divide by zero
    print(result)
except ZeroDivisionError as error:
    print("ZeroDivisionError:", error)
except ValueError as error:
    print("ValueError:", error)
except NameError as error:
    print("NameError:", error)
finally:
    print("I will be executed any How")

#
# try:
#     x = int(input("Enter a Number!!"))
#     result = 10 / x  # Attempting to divide by zero
#     print(result)
# except Exception as error:
#     print("Exception:", error)
# finally:
#     print("I will be executed any How")
#
# try:
#     x = int(input("Enter a Number!!"))
#     result = 10 / x  # Attempting to divide by zero
#     print(result)
# except Exception as error:
#     print("Exception:", error)

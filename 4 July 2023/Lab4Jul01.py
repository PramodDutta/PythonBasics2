x = int(input("Enter a number: "))
result = 10 / x
print(result)


# - Divide by Zero - ZeroDivisionError: division by zero
# - String or nothing - ValueError: invalid literal for int() with base 10: 'Pramod'
# - Negative -- Fine
# None - ValueError: invalid literal for int() with base 10: 'None'
# Float - ValueError: invalid literal for int() with base 10: '43.23'
# Complex - 1+8j - ValueError: invalid literal for int() with base 10: '1+8j'
# AB123 - ValueError: invalid literal for int() with base 10: 'ABC123'
# 100000000000000000000 - Very big value if int
# True - ValueError: invalid literal for int() with base 10: 'True'
# !!@#$ - ValueError: invalid literal for int() with base 10: '!@$@#@#'
# [], () - ValueError: invalid literal for int() with base 10: '[1,2,3,4]'
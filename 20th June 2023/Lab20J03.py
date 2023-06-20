# str + str  Ok
# int + int - Ok
# int + str - Problem


num1 = int(input("Enter a Number"))
num2 = int(input("Enter second Number"))
r = num1 + num2
print("Anwser is -> " + str(r))  # str+int
print("Anwser is -> ", r)  # Conversion Not required!!


bool_val = str(True)
print(bool_val)
# Create a Program with will take a user input and 2^num
# num**2 or pow(2,num)

user_input = input("Enter a Number and I will do num^2\t")
user_input = int(user_input)

# def pow_by_2(num):
#     return pow(2, num)
#
#
# result = pow_by_2(user_input)
# print(result)


result = lambda num: pow(2, num)
print(result(user_input))



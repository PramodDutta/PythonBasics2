bool_val = int(False)
print(bool_val)

# Int(True) ->  1, for False ->0


#Str to Int
string_num = int("10") # Base - 10
print(string_num)
print(type(string_num))

binary =  int("1010",2) # binary will be base - 2
print(binary)

octal = int("12",8)
print(octal)

hex_de = int("A",16)
print(hex_de)


ran_val =  int("@!24") # ValueError: invalid literal for int() with base 10: '@!24'
print(ran_val)

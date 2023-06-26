# JSON
#  It is commonly used for transmitting data in web applications
# {
#     "username":"93npu2yyb0@esiix.com",
#     "password":"Wingify@123",
#     "remember":false,
#     "recaptcha_response_field":""
# }
# json -> dic
# Hashmap -> json

# API - JSON -> dic in python if you want to work it
# data from py dic -> json -> transfer server.

# JSON - English / Networking
# dic - Hindi
# Me JSON -> Dic (  English -> Hindi)
# dic -> json ->

my_dict = {}
print((my_dict))
print(type(my_dict))

# dic , json

my_dict = {"name": "Alice", "age": 25}
print(my_dict)

# Accessing Values:

print(my_dict["name"])  # Output: Alice

# Updating Values:
my_dict["age"] = 26
print(my_dict)

my_dict = {"name": "Alice", "age": 25, "age2": 25}
print(my_dict)

# No Duplicates Keys
# Duplicates values are allowed.

my_dict["city"] = "New York"
print(my_dict)

# Deleting Key-Value Pairs

del my_dict["age"]
del my_dict["age2"]
print(my_dict)

# Mixed Dic
my_dict = {"name": "Pramod", "age": 32, "isMale": True, "Bal": 10.45}
print(my_dict)

# my_dict = {'C': "Pramod", 2: 32}
# print(my_dict)
# print(type(my_dict))

# keys can be of any data Type - int, float, str, bool, None

# my_dict = {"l_students": [1, 2, 3, 4], "l_students2": [5, 6, 7, 8]}
# my_dict = {"t_students": (1, 2, 3, 4), "t_students2": (5, 6, 7)}

# my_dict = {
#     "dict1": {"name": "Alice", "age": 25},
#     "dict2": {"name": "Bob", "age": 30},
#     "dict3": {"name": "Charlie", "age": 35},
# }
# print(my_dict)
# print(my_dict["dict3"]["age"])

my_dict = {"name": "Pramod", "age": 32, "isMale": True, "Bal": 10.45}
print(my_dict)


for key in my_dict:
    print(key)
    #print(key, my_dict[key])


if "name" in my_dict:
    print("Name is a key in the dictionary")


print(my_dict.get("name"))
print(my_dict["name"])


print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
# Check if a Key Exists in a Dictionary


dictionary = {"a": 1, "b": 2, "c": 3}


def check_present(a):
    return a in dictionary


print(check_present("a"))
print(check_present("z"))


# Remove a Key from a Dictionary

def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary


print(remove_key(dictionary, "b"))

dictionary = {"b": 1, "a": 2, "c": 3}


def sort_my_dict(dictionary):
    return dict(sorted(dictionary.items()))


print(sort_my_dict(dictionary))

#Find the Maximum Value in a Dictionary:

print(max(dictionary.keys()))
print(max(dictionary.values()))
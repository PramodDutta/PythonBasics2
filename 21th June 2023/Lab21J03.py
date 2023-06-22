my_list = [1, 2, 3, 4]


def is_even(x):
    return x % 2 == 0


# even_number = filter(is_even, my_list)
even_number = filter(lambda x: x % 2 == 0, my_list)
print(even_number)
even_number = list(even_number)
print(even_number)

# Filter -> 100 -> X (less 100)

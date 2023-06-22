# List Built In Func

my_list = [1,2,3]
# Index
print(my_list[0])

# Slicing
print(my_list[0:2])
print(my_list[2:])
print(my_list[:])
print(my_list[:-1])
print(my_list[:-2])

my_list.extend([4,5])
print(my_list)


# Insert, Remove

#Pop = Remove an item
i = my_list.pop(1)
print(i)
print(my_list) # Mutable - changeable
my_list.append(5)
print(my_list)

print(my_list.count(5))
print(my_list.count(7))
my_list.reverse()
print(my_list)


my_list.pop()
print(my_list)


N_LIST = [[1], [2,3], [4,5,6]]
print(N_LIST)
my_list = [52, 21, 56]
print(my_list)
my_list[0] = 31
print(my_list)

# List Mutable - IT can changed!!

# Tuple () - Immutable
car = ("i10", "XUV700", "Safari")
print(car)
print(car[0])
print(car[2])
# car[0] = "i20"
print(car)

print(car[0:2])
print(car[:])
print(car[:-1])
print(car[::-1])
print(len(car))

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

Tuple1 = tuple('Pramod')
print("\nTuple with the use of function: ")
print(Tuple1)

# Unpack
tuple1 = (3, 4, 5)
a, b, c = tuple1
print(a)
print(b)
print(c)

# Duplicate is allowed?
dup = [33, 33, 44, 55, 55]
t_dup = tuple(dup)
print(t_dup)

del t_dup
#print(t_dup)




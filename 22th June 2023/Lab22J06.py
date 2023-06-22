# Set
# Set is an unordered collection of data types.
# {}
lis = [1, 2, 3, 4, 5, 1]
my_set = set(lis)
print(my_set)

empty_set = set()
print(empty_set)

non_empty_set = set("Pramod")  # P r a m o d
print(non_empty_set)

# Creating a Set with
# the use of a List
set1 = set(["Prmaod", "Lucky", "Golu"])
print(set1)

# Creating a Set with
# the use of a tuple
t = ("TheTestingAcademy", "for", "TheTestingAcademy")
print("\nSet with the use of Tuple: ")
print(set(t))

set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy."])
set2 = set([123, "For", "TheTestingAcademy."])
print("\nInitial set")
print(set1)


for i in set1:
    print(i,end=" ")

for i in set2:
    print(i,end=" ")



set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

# Removing elements from Set
# using Remove() method

set1.remove(5)
set1.remove(6)
print(set1)


# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6,
			7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

# Removing element from the
# Set using the pop() method
set1.pop()
print("\nSet after popping an element: ")
print(set1)

set1.clear()
print(set1)


set10 = {"Pramod","Lucky","Amit","Pramod","AA"}
# set10.pop()
# print(set10)
set10.remove("Pramod")
print(set10)





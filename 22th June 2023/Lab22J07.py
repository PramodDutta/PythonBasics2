# Creating a Set
String = ('H', 'e', 'W', 'k', 'Q', 'F', 'o', 'P')
Fset1 = frozenset(String)
print("The FrozenSet is: ")
print(Fset1)

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.intersection(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.difference(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
subset = set2.issubset(set1)
superset = set1.issuperset(set2)
print(subset)
print(superset)
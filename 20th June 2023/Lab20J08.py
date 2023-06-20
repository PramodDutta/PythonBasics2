# List - []
# Store the elements
# different data types
# List items are changeable - (mutable)

# Create a List
my_marks = []
# my_marks2 = list()
print(type(my_marks))
# print(type(my_marks2))


my_marks.insert(0, 91)  # 91
my_marks.insert(1, 97)  # 91,97
my_marks.insert(1, 77)  # 91,77,97
print(my_marks)

#
#
# my_marks.clear()
# print(my_marks)

my_marks.append(89)
print(my_marks)

print(len(my_marks))

# my_marks.remove(91)
my_marks.remove(91)
print(my_marks)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0])
print(nested_list[1])
print(nested_list[2])

nested_list[0] = ["abc", "ef", "gh"]
print(nested_list)

dup_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(dup_list)

mix_list = ["apple", 123, True]
print(mix_list)


# Create range
sq = [i**2 for i in range(10)]
print(sq)

num = list(range(1,10))
print(num)
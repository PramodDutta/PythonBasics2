# Remove duplicates from list.

# non_dup = [33, 23, 44, 56]


# Normal Logic
# Go through the all items if item is present in the list, add to new non_dup_list

# Go through the all items - for loop
# if item is present in the list - if x not present
# non_dup_list.append - add to list
my_list = [33, 23, 23, 44, 56]
non_dup = []
for i in my_list:
    if i not in non_dup:
        non_dup.append(i)

# Fancy way to the task - Expression
# [non_dup.append(i) for i in my_list if i not in non_dup]
# We do this program in Java - it is difficutl if you use the square [expression]
# sw [] to Other Java.



print(non_dup)

# Set Functions
# Set - list of unordered and unique items
non_dup2 =  list(set(my_list))
# print(non_dup2)
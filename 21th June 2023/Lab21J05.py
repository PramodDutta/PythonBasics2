normal_list = [1, 2, 3, 4]

a = [[2, 3, 4], [5, 6, 7], [8, 9], [10]]

a.append([55,66])
a.extend([45,76])
a[0].reverse()
print(a)

print(a)



# Len -> 4
# print(len(a))
# print(len(a[1]))
# print(len(a[2]))
# print(len(a[3]))
#
print(a[2][1])

# for row in a:
#     print(row)


# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j],end=" ")
#     print()
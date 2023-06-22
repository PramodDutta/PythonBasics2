def do_something(a):
    return pow(2, a)  # 2^3 -> ?


numbers = [2, 3, 4]
result = list(map(do_something, numbers))
print(result)

# for i in result:
#     print(i)
r = []
for i in numbers:
    temp = do_something(i)
    r.append(temp)

print(r)

#Map - 100 ->  100 True

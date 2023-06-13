a = int(input("Enter value of a"))
b = int(input("Enter value of b"))
c = int(input("Enter value of c"))

# result = max(a,b,c)

# a > b && a > c ->  a
# b > a && b > c -> b
# c

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

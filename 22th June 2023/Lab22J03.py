# Check if two lists are identical.
# If all elements are present in the list
# len and sort - values will same


lis1 = [1, 2, 3]  # First list
lis2 = [3, 1, 2]  # Second list

if len(lis1) == len(lis2):
    lis1 = sorted(lis1)
    lis2 = sorted(lis2)
    if lis1 == lis2:
        print("Identical")
    else:
        print("Non Identical")

else:
    print("Non Identical")

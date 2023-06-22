# Using a Built In
my_list = [67, 98, 56]
max_result = max(my_list)
print(max_result)

# Sort and Last element
sort_result = sorted(my_list)  # 56,67,98
print(sort_result[len(sort_result) - 1])


# Comparing with each element
def find_large_element(numbers):
    large_element = numbers[0]
    for number in numbers:
        if number > large_element:
            large_element = number
    return large_element


result = find_large_element(my_list)
print("Large Number is", result)

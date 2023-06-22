# 1. How to check if a list is empty in Pythonm

my_list = []
non_list = [2, 3, 4]


def check_list(temp_list):
    if len(temp_list) == 0:
        print("List is empty")
    else:
        print("List is non empty")


check_list(my_list)
check_list(non_list)

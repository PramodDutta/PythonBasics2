#  Lucky Number with the 3 tries
# 1 to 10

import random

lucky_no = random.randint(1, 10)

guess_no = None

while guess_no != lucky_no:
    guess_no = int(input("Enter the Number from 1 to 10"))
    if guess_no < lucky_no:
        print("Too Low")
    elif guess_no > lucky_no:
        print("Too High")

print("Found the Number" + str(lucky_no))

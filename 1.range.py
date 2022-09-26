### Question 1
# Level 1

# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.


import math

first_num = 2000 + (7 - math.ceil(2000 % 7))

for i in range(first_num, 3022, 7):
    if i % 5 > 0:
        print(i, end=",")

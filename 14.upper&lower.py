# ### Question 14
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

input = input()
UPPER = LOWER = 0

for item in input:
    if item.islower():
        LOWER += 1
        continue
    if item.isupper():
        UPPER += 1
        continue

print("UPPER CASE:", UPPER)
print("LOWER CASE:", LOWER)

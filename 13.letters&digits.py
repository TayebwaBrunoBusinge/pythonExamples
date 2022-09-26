# ### Question 13
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

input = input()

inputJoined = "".join(input)
LETTERS = DIGITS = 0

for item in inputJoined:
    if item.isdigit():
        DIGITS += 1
        continue
    if item.isalpha():
        LETTERS += 1
        continue

print("LETTERS:", LETTERS)
print("DIGIT:", DIGITS)

# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010


nums = [int(("0b" + i), 2) for i in input().split(sep=",")]

divisible = [j for j in nums if (j % 5 == 0)]

for k in divisible:
    print(str(bin(k))[2:])

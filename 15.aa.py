# ### Question 15
# Level 2

# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

a = input()
sum = 0
for num in range(1, 5):
    sum = sum + int(a * num)
print(sum)

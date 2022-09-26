# ### Question 12
# Level 2

# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.


wanted = [
    str(i)
    for i in range(1000, 3000, 2)
    if float(str(i)[0]) % 2 == 0
    and float(str(i)[1]) % 2 == 0
    and float(str(i)[2]) % 2 == 0
    and float(str(i)[3]) % 2 == 0
]

print(",".join(wanted))

# Alternatively........#
#                      #
# This could also work.#
#                      #
#                      #
# .....................#

legible = {0, 2, 4, 6, 8}

wanted1 = [
    str(i)
    for i in range(1000, 3000, 2)
    if (int(str(i)[0]) in legible)
    & (int(str(i)[1]) in legible)
    & (int(str(i)[2]) in legible)
    & (int(str(i)[3]) in legible)
]
print("\nMethod 2:\n")
print(",".join(wanted1))

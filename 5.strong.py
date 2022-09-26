### Question 5
# Level 1

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters


class strong(object):
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Hit me: ")

    def printString(self):
        print(self.string)


string = strong()
string.getString()
string.printString()

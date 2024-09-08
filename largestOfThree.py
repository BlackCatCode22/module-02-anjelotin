# Angelo Andrade
# largestOfThree.py
# 9/8/24
# Write a Python program that uses nested if statements (nested decisions) to get three integers from the user and outputs the largest of the three.

# Variables for three integers users
myNumOne = 0
myNumTwo = 2
myNumThree = 0
largest = 0

# Output
if (myNumOne > myNumTwo) :
    if (myNumOne > myNumThree) :
        largest = myNumOne
        print(largest, "is the largest")
elif (myNumTwo > myNumThree) :
    largest = myNumTwo
    print(largest, "is the largest")
else:
    largest = myNumThree
    print(largest, "is the largest")

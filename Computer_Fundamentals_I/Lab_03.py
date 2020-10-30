"""
*Write a program that generates four integers between -50 and +50 and displays the calculations noted below.
"""

import random

# Ranges
negativeRange = -50
positiveRange = 50

# Variables containing 4 diffrent random integers
randomOne = random.randint(negativeRange, positiveRange)
randomTwo = random.randint(negativeRange, positiveRange)
randomThree = random.randint(negativeRange, positiveRange)
randomFour = random.randint(negativeRange, positiveRange)

# Max & Min Integers
maxInteger = max(randomOne, randomTwo, randomThree, randomFour)
minInteger = min(randomOne, randomTwo, randomThree, randomFour)

# Even & Odd
is_even = 0
is_odd = 0
if (randomOne % 2 == 0):
    is_even += 1
else:
    is_odd += 1
if (randomTwo % 2 == 0):
    is_even += 1
else:
    is_odd += 1
if (randomThree % 2 == 0):
    is_even += 1
else:
    is_odd += 1
if (randomFour % 2 == 0):
    is_even += 1
else:
    is_odd += 1

# Numbers greates than -25 but less than 25
is_in_range = 0
if -25 < randomOne and randomOne < 25:
    is_in_range += 1
if -25 < randomTwo and randomTwo < 25:
    is_in_range += 1
if -25 < randomThree and randomThree < 25:
    is_in_range += 1
if -25 < randomFour and randomFour < 25:
    is_in_range += 1

# Number of positive integers &  Number of negative integers
is_positive = 0
is_negative = 0
if randomOne > 0:
    is_positive += 1
else:
    is_negative +=1
if randomTwo > 0:
    is_positive += 1
else:
    is_negative +=1
if randomThree > 0:
    is_positive += 1
else:
    is_negative +=1
if randomFour > 0:
    is_positive += 1
else:
    is_negative +=1

# Average of smallest inetegers &  Largest integer
averageOfSmallAndLargeInteger = (minInteger + maxInteger) / 2

#Average of all integers
averageOfRandomNumbers = randomOne + randomTwo + randomThree + randomFour / 4

# Print Values
print("Random integers: ", randomOne, randomTwo, randomThree, randomFour)
print("The maximum integer is: ", maxInteger)
print("The maximum integer is: ", minInteger)
print("The number of evens is: ", is_even)
print("The number of odds is: ", is_odd)
print("The numbers greates than -25 but less than 25 is: ", is_in_range)
print("The number of positive integers is: ", is_positive)
print("The number of positive integers is: ", is_negative)
print("The average of the smallest and largest integers is: ", averageOfSmallAndLargeInteger)
print("The average of all inetgers is: ", averageOfRandomNumbers)


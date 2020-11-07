"""
Program Lab 05
"""
import random
import math

array = []  # Create an empty array

negativeRange = -100
positiveRange = 100

j = 0
n = 25  # size of the array
while (j < n):  # populate the array using the while loop
    arrayNumbers = random.randint(negativeRange, positiveRange)  # Return a random integer  a <= x <= b.
    array.append(arrayNumbers)  # APPEND adds to a list
    j = j + 1

print("Array list:", array)  # (2) now print the array
print("The lenght of the array is:", len(array))

# Even & Odd Numbers
even_count = 0
odd_count = 0
for i in array:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("The numbers of even numbers in the array is:", even_count)
print("The numbers of odd numbers in the array is:", odd_count)

# Numbers greater than zero & less than zero
greater_than_zero = 0
less_than_zero = 0
for y in array:
    if y > 0:
        greater_than_zero += 1
    else:
        less_than_zero += 1
print("The numbers greater than zero in the array is:", greater_than_zero)
print("The numbers greater than zero in the array is:", less_than_zero)

# Median
median = sorted(array)[len(array) // 2]
print("The median of the array is:", median)

# Integers >= median
integers_after_array = sorted(array)
after_numbers = integers_after_array[len(array)//2:len(array)]
print("The integers equal and after the median are: ", after_numbers)

#Display the integers  <  median
integers_before_array = sorted(array)
before_numbers = integers_before_array[0:len(array) //2]
print("The integers equal and after the median are: ", before_numbers)

# Ask the user for an integer and print the number of times the integer is in the list
num = int(input("Please enter integer to see if it is on th array: "))
print(num, " is in the array for a total of ", array.count(num))

# Display MAX and MIN integer
maxValue = max(array)
minValue = min(array)
print("The maximum integer in the array is: ", maxValue)
print("The minimum integer in the array is: ", minValue)

# Display the list in reverse sorted order (largest to smallest) See the sort() and reverse() functions
array.sort()
array.reverse()
print("The sorted array largest to smallest is", array)

#Display GCD
largest_number = array[0]
smallest_number = array[len(array)-1]
gcd_out = math.gcd(largest_number,smallest_number)
print("The GCD of the largest an smallest integer is:", gcd_out)

"""
*Name: Alan Ivan Jimenez Gallardo
*Instructor: Witold Sieradzan
*Assignment: Lab09
*Due: 12/01/2020
"""

import random


def fill(nx, x, y):
    lx = []
    j = 0
    while (j < nx):
        randNum = random.randint(x, y)
        if randNum not in lx:
            lx.append(randNum)
            j = j + 1
    return lx


def display(lx):
    for number_in_array in range(len(lx)):
        if (number_in_array + 1) % 5 == 0:
            print('{:2d}'.format(lx[number_in_array]))
        else:
            print('{:2d}'.format(lx[number_in_array]), end=' ')


def maxValue(lx):
    return max(lx)


def minValue(lx):
    return min(lx)


def ave(lx):
    average_of_list = sum(lx) / len(lx)
    return average_of_list


def sum(lx):
    sum_values = 0
    for index in range(len(lx)):
        sum_values = sum_values + lx[index]
    return sum_values


def div3(lx):
    count_div3 = 0
    for x in lx:
        if x % 3 == 0:
            count_div3 += 1
    return count_div3


def evens(lx):
    count_evens = 0
    for x in lx:
        if x % 2 == 0:
            count_evens += 1
    return count_evens


def odds(lx):
    count_odds = 0
    for x in lx:
        if x % 2 != 0:
            count_odds += 1
    return count_odds


def digit1x(lx):
    count_digit_start_one = 0
    for x in lx:
        if x // 10 == 1:
            count_digit_start_one += 1
    return count_digit_start_one


def digitx1(lx):
    count_digit_end_one = 0
    for x in lx:
        if x % 10 == 1:
            count_digit_end_one += 1
    return count_digit_end_one


def median(lx):
    median = sorted(lx)[len(lx) // 2]
    return median

def sortDescending(lx):
    return sorted(lx, reverse=True)


def mlxMinAverage(lx):
    mlxMinAVG = (maxValue(lx)+minValue(lx))/2
    return mlxMinAVG


def FirstLast(mx, mnx):
    first_int = max(str(mx))
    last_int = str(mnx)
    first_and_last = first_int[0] + last_int[len(last_int) - 1]
    first_and_last = int(first_and_last)

    return first_and_last


def randomCount(lx, zx):  # note
    if zx in lx:
        return 'Yes, the number is in the list'
    else:
        return 'Not in the list'


# NOW we call the functions using Lab10Driver.py
# Lab10Driver.py
# calls the functions in Lab10Template.py

# from Lab10Template.py import *   # IMPORTANT
n = 25
a = 10
b = 60
myList = fill(n, a, b)
print("1- populating my list ", myList)
print("2- the list (5 lines)")
display(myList)

# display the list in descending sorted order
myList = sortDescending(myList)
print("3- the sorted array largest to smallest is:", myList)

# sum mlx min average
m = maxValue(myList)
mn = minValue(myList)
s = sum(myList)
average = ave(myList)
# even and odds
e = evens(myList)
o = odds(myList)

print("4- The total Sum is", s)
print("5- The Minimum Value is", mn)
print("6- The Maximum  Value is", m)
print("7- The Average is", average)
print("8- The number of even integers is", e)
print("9- The number of odd integers is", o)

# as a first digit and 1 as a last digit
x = digit1x(myList)
print("10- The number of integers start with the digit 1 is", x)
y = digitx1(myList)
print("11- The number of integers end with the digit 1 is", y)

# number of didgits divisible by 3
z = div3(myList)
print("12- the number of integers divisible by 3 with no remainder is", z)

# median calculations
m = median(myList)
print("13- The median of the list is", m)

# average of min and mlx
mave = mlxMinAverage(myList)
print("14- The average of the maximum and minimum is", mave)

# randomCount implementation
# using the return value function maxValue(myList) == m
# and the return value mn of the function minValue(myList)
z = FirstLast(m, mn)
print('15 the integer formed by first digit + lastdigit == ', z)

c = randomCount(myList, z)
print("16 the number ", z, 'in the list ?? ', c)

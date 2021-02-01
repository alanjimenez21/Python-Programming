"""
PROBLEM 1

A hotdog stand sells hotdogs, potato chips and sodas.  Hotdogs are $2.50 each.
Potato chips are $1.50 per bag.  Sodas are $1.25 per cans.
Design a program to do the following.  Ask the user to enter number of hotdogs, chips and sodas ordered
by the customer.  The program will calculate and display the total amount due.
"""

#Define Variables
hot_dogs = 2.5
potato_chips = 1.5
sodas = 1.25

#Prompt the user to input amounts
print("Welcome to Fair Eatings!")
count_hot_dogs = int(input("How many hot dogs would you like? "))
count_potato_chips = int(input("How many potato chips would you like? "))
count_sodas = int(input("How many sodas would you like? "))

#Calculations
total_hot_dogs = hot_dogs * count_hot_dogs
total_potato_chips = potato_chips * count_potato_chips
total_sodas = sodas * count_sodas
amount_due = total_hot_dogs+total_potato_chips+total_sodas

#Display Amount
print("Your total amount due is $", amount_due)

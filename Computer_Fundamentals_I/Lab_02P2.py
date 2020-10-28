"""
*Write a Python program that provides a solution for Problem #8 in Quiz 00 Recall the problem read as follows:
Aaron is staying at a hotel that charges $100 per night plus tax for a room.  A tax of 8% is applied to the room
rate per day and an additional one-time fee of $5.00 is charged by the hotel.  Which of the following represents
total charge, in dollars, for staying x nights
"""

#Fixed Variables
taxRate = .08   # tax for each day
oneTimeFee = 5.00 # one time fee
roomCost = 100  # room rate

#Prompt user to enter days reserved at hotel
daysReserved = int(input("Enter the number of days stayed at the hotel: "))

#If & Else Statement with mathemtical solution
if (daysReserved > 0):
    totalCost = (1+taxRate) * (roomCost * daysReserved) + oneTimeFee
    print("The cost for ", daysReserved, " days  is  ", totalCost )
else:    # here d <= 0
    print("Invalid entry for days: ", daysReserved )

"""
PROBLEM 3

Admission to an aquarium is $14 per person.
There is also an IMAX theatre in the building, which charges $8 per ticket for a 3D shark show.
Customers have three choices: admission to the aquarium only without watching 3D show, watch 3D show
only with no admission to the aquarium, or do both with a 25% discount.  Design a program for group orders.
Ask the group to enter number of people who want admission only but no 3D show, number of people who want 3D show
only but no admission to the aquarium, and number of people who want both.  Calculate and display the
total amount due from the group.
"""

#Variables
aquarium_ticket = 14
theater_ticket = 8


#Prompt user
count_aq_ticket = int(input("How many tickets would you like for the aquarium only? "))
count_show_ticket = int(input("How many tickets would you like for the show only? "))
count_both = int(input("How many tickets would you like to include both aquarium and show? "))

#Calculations
price_aq_tickets = aquarium_ticket*count_aq_ticket
price_show_tickets = theater_ticket*count_show_ticket
price_both = (14+8)*(count_both)-((14+8)*(count_both)*.25)
total_amount = price_aq_tickets +price_show_tickets+price_both

#Display totals
print("The total amount due for all the tickets is", total_amount)

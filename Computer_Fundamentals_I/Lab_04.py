"""
*Provide a python program to determine the parking fees at the airport based on the following time constraints
"""


#Initialize Variables
fee = 0  # initialize
f1 = 5  # table 1 fee
f2 = 4  # table 2 fee
f3 = 2  # table 3 fee

#User Input
m = int(input("Please enter number of minutes parked..."))

# table 1
if (0 < m and m <= 60):  # table 1
    #  hrs = int(m/60) + 1
    fee = f1
    print("Parking fee for ", m, " minutes is $", fee)

# now for table 2
elif (m > 60 and m <= 300):  # table 2
    if (m % 60 ==0):
        fee = (int(m / 60)) * f2
        print('we are in table 2 fee is $', fee)
    else:
        fee = (int(m / 60) + 1) * f2
        print('we are in table 2 fee is $', fee)

# now table 3
elif (m > 300):  # table 3
    if (m % 60 == 0):
        fee = (int(m / 60)) * f3
        print('we are in table 3 fee is $', fee)
    else:
        fee = (int(m / 60) + 1) * f3
        print('we are in table 3 fee is $', fee)
else:
    print("error  negative minutes", m)

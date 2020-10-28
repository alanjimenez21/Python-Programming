"""
*Write a Python program that determines cell phone charges
(problem #1 in quiz 00 with the stipulation that the user can use their phone < 300 minutes.
"""

#Fixed Variables
fixedPrice = 30
additionalFee = .45  # initialize cost variable

#Prompt User to enter minutes consumed
numberOfMinutes = int(input("Enter the number of minutes: "))

#If & Else Statement with mathemtical solution
if (numberOfMinutes > 300):
    totalCost = fixedPrice + (numberOfMinutes - 300) * additionalFee
    print("The cost for ", numberOfMinutes, " minutes  is: ", totalCost)
else:  
    print("The cost for ", numberOfMinutes, " minutes is: ", fixedPrice)

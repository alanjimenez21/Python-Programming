"""
*Program for Lab06
"""
import random
import math


temp = -1
n = 50
nn = 1000 # note nn*n == 50000
p = .5

#Theorical Math
u = n*nn*p
v = u*(1-p)
sd = math.sqrt(v)

# Theoretical calculations
print('======Theoretical results (what is expected) ==========')
#Using the Binomial distribution formulas on page 1
print('1 The theoretical mean(average)of 1''s ( n*nn*p) ==', u)
print('2 The theoretical variance v  == ', v)
print('3 The standard deviation SD (should be > 100)  == ', sd)
#  sd = square root(v)
#  at this point in the code
#  we have the theoretical mean, variance, standard deviation
# now for the experimental results
print(' ========== Experimental results ========== ')
print(' ========== Populate a list and count 1’s = ')
temp = -1
a = 0
b = 1
MyList = []
j = 0
while (j < nn):    # loop for 1000 times
    i = 0
    while i < n :    # loop 50 times populate list of nn
        randNum = random.randint(a,b)
        MyList.append(randNum)
       #  count the number of 1’s and the number of 0
       #  use the count function
       #  the number of 1’s + number 0’s == 50
       #  keep track of these counts and update the results
       # with the next iteration
        i = i +1
    j = j + 1

count_ones = MyList.count(1)
count_zeroes = MyList.count(0)
average_of_total = (count_ones/(n*nn))

print('4 the length of MyList == ', len(MyList))       # FIX use len()
print('5 the number of 1’s is ==', count_ones  )       # FIX
print('6 the number of 0’s is ==', count_zeroes  )        # fix
print('7 the average of all the ==', n*nn,' integers  is...',
        'should be < 1) ==', average_of_total)         # fix
print()

# fix SD = sqrt(v)
sd = math.sqrt(v)
two_sd = sd*2
variable_mean_minus = u - two_sd
variable_mean_plus = u + two_sd

# Display the range (+- 2sd ) as follows:
# mean == number of 1’s + 2*SD  mean – 2*SD
print('8 number of 1 - 2*SD == ', math.floor(variable_mean_minus))    #fix
print('9 number of 1 + 2*SD == ', math.floor(variable_mean_plus))    #fix
# Answer the question:
# is the total number of 1’s from 5 above within the limits
#  mean – 2*SD < mean < mean + 2*SD true ?  Yes or no
# within the range as calculated in 8 and 9 by printing
#‘Yes’ if it is within the range  and
# ‘No’   if it is not within the range
answer= ""
if(u - math.floor(variable_mean_minus)< u < u + math.floor(variable_mean_plus)):
    answer = "Yes"
else:
    answer = "No"
print('10 Is the number of 1''s within +- 2*SD== ', answer)  # FIX

#Display 10 lines, 25 integers per line of the n*nn (== 50000) integers
# That is, display the integers in MyList, 25 per line, for 10 lines
# and include the line number as in 1 , 2, 3, …10
# NOTE only display 10 lines with 25 values (= 0 or 1)
# and not all 50,000 integers
print('11 displaying 10 numbered lines with 25 integers per line ...')
# for your consideration will need adjustments
k = 0
sub = []
num = 0
while (k < len(MyList) ):
    sub = MyList[k: k+25]    # Splice
    num+=1
    print(num,"...", sub)      # do NOT print k only the
                                # line number as in 1, 2,3
    k = k+5000

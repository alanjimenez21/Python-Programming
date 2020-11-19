"""
*Assignment: Lab07
"""

a = [ "Euclid", "Archimedes", "Newton","Descartes", "Fermat", "Turing", "Euler", "Einstein", "Boole", "Fibonacci", "Nash"]
vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U','u']

#Print the longest name
maxlen =0
for k in a:
    if len(k)> maxlen:
        maxlen = len(k)
        t = k
print("The longets name in the array is: ", t, " with a length of ", len(t)), " charcaters"

#Print the smallest name
minlen=0
for y in a:
    if len(k)<minlen:
        minlen = len(y)
        t = y
print("The smallest name in the array is: ",y," with a lenght of ",len(y)), " characters"

#Print the number of names in the array
print("The number of names in the array is:",len(a))

#Display a string that consists of the first letter from each of 11 names in the list
first_letter=0
print("The first letter for all the names in the array are: ",end=" ")
for letter in a:
    letter_one=a[first_letter][0]
    print(letter_one, end="")
    first_letter +=1

#Display a string that consists of the last letter from each of 11 names
print()
last_letter= 0
print("The last letter for all the names in the array are: ",end=" ")
for letter_end in a:
    letter_final=a[last_letter][len(a[last_letter])-1]
    print(letter_final, end="")
    last_letter +=1

print()
#Display the number of times the letter appears in the list
count=0
letter_input =input("Please enter a letter: ")
for letters in a:
    if(letters[0]==letter_input):
        count +=1
print("The number of times ",letter_input," is found in array totals: ",count)

#Sort list a and display the list  i.e. the first name in the list should be Archimedes; last name is Turing
a.sort()
print("The sorted array is ",a)

#Sort the list in reverse order and display the  list i.e. the first name should be Turing and the last Archimedes
a.reverse()
print("The reversed array is: ",a)

#Display the number of vowels using the vowels list in the list a (in operator may be useful)
count_vowels=0
for names in a:
    for i in range(len(names)):
        if names[i] in vowels:
            count_vowels +=1
print("The number of vowels in the array is: ",count_vowels)

#Add your  last name to the list and display the list in sorted order (your last name should be in the list
a.append("Jimenez")
a.sort()
print("The array list with my last name is now: ",a)

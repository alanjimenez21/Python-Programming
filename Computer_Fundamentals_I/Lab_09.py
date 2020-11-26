"""
"""

#1. Ask the user for a string and create the following dictionary
string = input("Please Enter a String: ")
d={}

for x in range(len(string)):
    d[x]=string[x]
#2. Display the length of the dictionary d using a len function In this case the answer  is 6
print("The lenght of the dictionary is:",d.__len__())

#3. Ask the user for a key(integer).  If the key is in the dictionary display the corresponding value.  As an example if the user entered 2 display ‘C’ if the user entered a key that was not in the dictionary display “Error key not found”
integer_key = int(input("Please enter an integer to display the letter in the dictionary: "))
if integer_key in d:
    print("The value for", integer_key,"is",d[integer_key])
else:
    print("Error key not found")

#4. Ask the user for a value (one of the characters in our example).  If the value is in the dictionary display “Value found” otherwise display “Value not found”.  As an example if the user entered ‘C’ display “Value found”
char_key = input("Please enter a char value to display the letter in the dictionary: ")
if char_key in d.values():
    print("Value Found")
else:
    print("Value not found")

#5. Ask the user for a character and add it to the dictionary.  As an example, if the user enters ‘X’ then the key should be the next integer (in this case 6 but in general it should be related to the length of the dictionary )  For this example
char_input = input("Enter a character to be added to the dictionary: ")
d[len(string)]=char_input
print("The dictionary with the extra character is:",d)

#6. Replace the last key: value combination with your last name.  Assuming your last name is Euler
d[len(d)-1]="Jimenez-Galalrdo"
print("The dictionary with my last name is:",d)

#7. Ask the user for a key and delete it and its corresponding value from the dictionary.  As an example, if the user enters 0 then the key and its value (0 : ’C’) should be deleted from the dictionary  If the key is not in the dictionary print 'key not found’.
delete_ch = int(input("Enter Key to Delete: "))
if delete_ch in d.keys():
    del d[delete_ch]
else:
    print("Error key not found")

print("The Dictionary with the deleted key is:", d)

#8. Ask the user for a string of digits, separated by commas.  Print out the corresponding values for those digits using the split function .
S = input("please enter integers separated by a , ")
S = S.split(',')

for z in S:
    z =int(z)
    if z in d.keys():
        print(d[x],end="")
    else:
        print("*",end="")

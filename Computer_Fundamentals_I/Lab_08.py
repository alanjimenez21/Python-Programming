"""
"""
names = ["Euclid", "Archimedes", "Newton", "Descartes", "Fermat",
         "Turing", "Euler", "Einstein", "Boole", "Fibonacci", "Lovelace",
         "Noether", "Nash", "Wiles", "Cantor", "Gauss", "Plato"]

# 1 Display a string that consists of the first letter and last letter from each of the names in the list
first_letter = 0
last_letter = 0
print("1-The first and last letters from every name in the array are: ", end=" ")
for two_letter in names:
    letter_one = names[first_letter][0]
    letter_final = names[last_letter][len(names[last_letter]) - 1]
    print(letter_one, end="")
    print(letter_final, end="")
    first_letter += 1
    last_letter += 1
print()
# 2.	Display  list names with all the names reversed that is display
print("2-The reversed names in the array are: ")

for q in names:
    #print(q[len(q)-1],q[len(q)-2],q[len(q)-3],q[len(q)-4],q[len(q)-5] ,q[0],", ", end=" ")

# 3.	Display the total number of characters in the list
count_characters = 0
for xrt in range(0, len(names)):
    for yrt in range(0, len(names[xrt])):
        count_characters += 1
print("3-There are", count_characters, "characters in the names array")

# 4. Display the number of consonants (non-vowels)
vowel = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
vowelCnt = 0
for k in names:
    j = 0
    while j < len(k):
        if k[j] in vowel:
            vowelCnt = vowelCnt + 1
        j = j + 1
print("4-The number of consonants in the names array is:", count_characters - vowelCnt)

# 5. Display alphaCnt which contains the number of each letter in the list
alphaCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for alpha_letters in names:
    for ch in alpha_letters:
        x = ord(ch.upper()) - ord('A')
        alphaCount[x] = alphaCount[x] + 1
print("5-The Alpha Count is: ", alphaCount)

# 6.	Display the average length of all the entries in the list names.
avLen = count_characters / len(names)
print("6-The average of the lenght of all entries is: ", avLen)

# 7.	Once you have populated alphaCnt (== number of letters in the list names) display the letter  that occurs the most  in alphaCnt
i = 4
print("7-The letters that display the most is: ", chr(65+i))

# 8.Once you have populated alphaCnt (== number of letters in the list names) display the letters that have a value of zero besides Y and Z
print("8-The letters that have zero are: ", chr(74),chr(75),chr(81),chr(88))

# 9.Sort the list names and display the median name Do not use constants as 8 or 9 use integer  division with the n = len(names)
median_name=len(names)//2
median_name =names[median_name]
print("9-The Median name in the array is:", median_name)

# 10.Display the number of vowels in names Use the results from 3 and 4 above
vowel = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
vowelCnt = 0
for k in names:
    j = 0
    while j < len(k):
        if k[j] in vowel:
            vowelCnt = vowelCnt + 1
        j = j + 1
print("10-The number of vowels in the names array is:", vowelCnt)

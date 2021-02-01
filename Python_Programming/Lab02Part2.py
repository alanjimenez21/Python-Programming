"""

PROBLEM 2

Each student in a course needs to submit 3 lab assignments and take 2 tests.
Design a program to do the following.  Ask the user to enter 3 lab scores and 2 test scores.
Calculate and display the lab average and the test average.
Also calculate and display the course grade, which equals 55% of the lab average plus 45% of the test average.
"""

# Prompt user to input scores
print("Course Grade")
lab1_score = int(input("Enter lab one score: "))
lab2_score = int(input("Enter lab two score: "))
lab3_score = int(input("Enter lab three score: "))
test1_score = int(input("Enter test one score: "))
test2_score = int(input("Enter test two score: "))

lab_avg = (lab1_score + lab2_score + lab3_score) / 3
test_avg = (test1_score + test2_score) / 2

final_lab_score = lab_avg * .55
final_test_score = test_avg * .45
course_grade = final_lab_score + final_test_score

print("The course grade is: ", course_grade)

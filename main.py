
# Prompting the user to enter the number of courses taken
stud_course = int(input("Please enter the number of course:? "))

# Prompting the user to enter their score for a course
score = int(input("Enter your score >>> "))

# Looping through each course taken
for i in range(stud_course):

    # Assigning a letter grade and grade point based on the score
    if score >= 80:
        letter_grade = "A"
        grade_point = 4.0
    elif score >= 60:
        letter_grade = "B"
        grade_point = 3.0
    else:
        letter_grade = "C"
        grade_point = 2.0

    # Printing the letter grade and grade point to the console
    print(f"You had grade point {grade_point} and letter grade as {letter_grade}")
































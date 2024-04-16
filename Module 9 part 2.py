# Zahri Sallette
# CIS 129
# This program reads grades from the 'grades.txt' file, displays individual grades, total, count, and average

# Open the file in read mode
with open('grades.txt', 'r') as file:
    # Read all lines from the file
    grades = file.readlines()

# Convert grades to integers and calculate total, count, and average
grades = [int(grade.strip()) for grade in grades]
total = sum(grades)
count = len(grades)
average = total / count

# Display individual grades, total, count, and average
print("Individual Grades:", grades)
print("Total:", total)
print("Count:", count)
print("Average:", average)

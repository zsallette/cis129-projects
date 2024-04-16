# Zahri Sallette
# CIS 129
# This program prompts the user to enter grades and stores them in a plain text file called 'grades.txt'.

# Open the file in write mode
with open('grades.txt', 'w') as file:
    while True:
        # Prompt the user to enter grades
        grade = input("Enter a grade (or 'q' to quit): ")
        
        # Check if the user wants to quit
        if grade.lower() == 'q':
            break
        
        # Write the grade to the file
        file.write(grade + '\n')

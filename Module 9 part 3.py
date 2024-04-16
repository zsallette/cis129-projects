import csv

# Zahri Sallette
# CIS 129
# This program prompts the user to enter students first and last name and writes the records into a CSV file named 'grades.csv'.

# Open the file in write mode with newline='' to avoid extra newlines
with open('grades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    while True:
        # Prompt the user for student information
        first_name = input("Enter student's first name (or 'q' to quit): ")
        
        # Check if the user wants to quit
        if first_name.lower() == 'q':
            break
        
        last_name = input("Enter student's last name: ")
        exam1 = int(input("Enter exam 1 grade: "))
        exam2 = int(input("Enter exam 2 grade: "))
        exam3 = int(input("Enter exam 3 grade: "))
        
        # Write the student record to the CSV file
        writer.writerow([first_name, last_name, exam1, exam2, exam3])

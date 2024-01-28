# Lynn Prout
# MO2 Lab If_Else_While
# This program takes user input of first name, last name, and GPA
# to determine academic achievement level

def process_student_records():
    while True:
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
        if last_name == 'ZZZ':
            break

        first_name = input("Enter student's first name: ")
        
        gpa = float(input("Enter student's GPA: "))
        
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} did not qualify for the Dean's List or the Honor Roll.")
      
process_student_records()
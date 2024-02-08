"""Make a second version of the program above (average marks) and change it so
that all the names and marks are added to a list. In addition to the output
produced in the original version, this version should also calculate and print
each student's name and a 'University' style grade. University grades are
awarded as follows: A mark of 90% or more is an A+ grade. 85-89% is A. 80-84%
is A-. 75-79% is B+. 70-74% is B. 65-69% is B-. 60-64% is C+. 55-59% is C.
50-54% is C-. 40-49% is D. 0-39% is E."
"""

def number_checker(question):
    error = "\nYou must enter a valid number\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)

    total_marks = 0
    marks_list = []
    best_mark = 0
    best_student = []

    while True:
        name = input("Student name: ").title()
        if name == "X":
            break
        else:
            if len(name) < 2:
                print("The name must be at least 2 characters long")
                continue
            else:
                mark = number_checker(f"{name}'s mark: ")
                while not 0 <= mark <= 100:
                    print("Marks can only be between 0 and 100")
                    mark = number_checker(f"{name}'s mark:")
                else:
                    total_marks += mark
                    marks_list.append([name, mark])

    total_students = len(marks_list)
    for student in marks_list:
        if student[1] > best_mark:
            best_mark = student[1]
            best_student = [student]
        elif student[1] == best_mark:
            best_student.append(student)

    average_mark = round(total_marks/total_students, 2)
    print(f"\nThe average mark was {average_mark}")
    if len(best_student) > 1:
        print(f"The best students are:")
        for student in best_student:
            print(f"\t{student[0]}")
        print(f"\ttall with {best_student[0][1]} marks")
    else:
        print(f"{best_student[0][0]} was the best student, with a mark of "
              f"{best_mark}")

    print(f"\nThe complete list is: ")
    for student in marks_list:
        print(f"\t{student[0]}, with {student[1]} marks")

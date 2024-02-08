"""Your english teacher wants a program to keep track of their students marks
and grades. Write a program which takes, as input, the student's name and an
exam mark - between 0 and 100. The program should keep asking for input until
"X" is entered as the students name. The program should then output the name
and mark of the best student, as well as the average mark for all students.
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

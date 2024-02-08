"""Make a second version of the program above (average marks) and change it so
that all the names and marks are added to a list. In addition to the output
produced in the original version, this version should also calculate and print
each student's name and a 'University' style grade. University grades are
awarded as follows: A mark of 90% or more is an A+ grade. 85-89% is A. 80-84%
is A-. 75-79% is B+. 70-74% is B. 65-69% is B-. 60-64% is C+. 55-59% is C.
50-54% is C-. 40-49% is D. 0-39% is E.
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


def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif 85 <= mark < 90:
        return "A"
    elif 80 <= mark < 85:
        return "A-"
    elif 75 <= mark < 80:
        return "B+"
    elif 70 <= mark < 75:
        return "B"
    elif 65 <= mark < 70:
        return "B-"
    elif 60 <= mark < 65:
        return "C+"
    elif 55 <= mark < 60:
        return "C"
    elif 50 <= mark < 55:
        return "C-"
    elif 40 <= mark < 50:
        return "D"
    else:
        return "E"


def main():
    marks_list = []

    while True:
        name = input("Student name: ").title()
        if name == "X":
            break
        else:
            if len(name) < 2:
                print("The name must be at least 2 characters long")
                continue
            else:
                mark = number_checker(f"{name}'s mark - in percentage: ")
                while not 0 <= mark <= 100:
                    print("Marks can only be between 0 and 100")
                    mark = number_checker(f"{name}'s mark - in percentage: ")
                else:
                    marks_list.append([name, mark])

    total_marks = sum(mark for _, mark in marks_list)
    total_students = len(marks_list)

    best_mark = max(mark for _, mark in marks_list)
    best_students = [student for student in marks_list if
                     student[1] == best_mark]

    average_mark = round(total_marks / total_students, 2)

    print(f"\nThe average mark(percentage) was {average_mark}")

    print("The best students are:")
    for student in best_students:
        print(f"\t{student[0]} with {student[1]} marks(percentage)")

    print("\nUniversity Grades:")
    for student in marks_list:
        grade = calculate_grade(student[1])
        print(f"\t{student[0]} - {grade}")

    print("\nThe complete list is: ")
    for student in marks_list:
        print(f"\t{student[0]}, with {student[1]} marks(percentage)")


if __name__ == "__main__":
    main()

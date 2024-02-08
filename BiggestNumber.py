def number_checker(question):
    error = "\nYou must enter a number\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


while True:
    number_1 = number_checker("Enter the first number")
    if number_1 == 0:
        break
    else:
        number_2 = number_checker("Enter the second number")

    if number_1 == number_2:
        print(f"\nBoth numbers are {number_1}, therefore they are equal")
    elif number_1 > number_2:
        print(f"\nNumber {number_1} is the largest")
    else:
        print(f"\nNumber {number_2} is the largest")

print("The end")

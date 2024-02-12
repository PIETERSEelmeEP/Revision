"""Colossal Construction is a company which delivers concrete for the
foundations of new residential and commercial buildings. You have been asked
to write a program to calculate the volume of concrete needed for each job,
as well as the total needed for all jobs on a particular day. The foundations
for commercial buildings need to be 50cm thick, whereas those for residential
buildings are only half that thickness. The program should keep asking for
inputs and producing the volume results until a rogue building type ("x") is
entered. The program should then tell the user the total amount of concrete
needed for the day.
"""


def number_checker(question):
    error = "\nYou must enter a valid number\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


daily_volume = 0
COMMERCIAL = 50
RESIDENTIAL = 25

while True:
    building_type = input("Will this concrete be used for Residential or "
                          "Commercial buildings? \nEnter 'C' for Commercial or"
                          " 'R' for Residential or 'X' to exit: ").upper()
    if building_type == "X":
        break
    else:
        while building_type != "C" and building_type != "R":
            building_type = input("Please enter a valid building type\n Enter "
                                  "'C' for Commercial or 'R' for Residential "
                                  "or 'X' to exit: ").upper()

    length = number_checker("Enter the length of required concrete - in "
                            "centimeters: ")
    width = number_checker("Enter the width of required concrete - in "
                           "centimeters: ")

    area = length * width

    if building_type == "C":
        volume = area * COMMERCIAL
    else:
        volume = area * RESIDENTIAL

    print(f"The volume of concrete required for this building is {volume} "
          f"cubic centimeters\n")

    daily_volume += volume

print(f"\nThe total volume of the concrete required today will be "
      f"{daily_volume} cubic centimeters")
print("Bye")

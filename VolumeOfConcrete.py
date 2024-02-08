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

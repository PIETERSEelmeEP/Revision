"""The numbers of calories burned per hour by bicycling, jogging, swimming are
200, 475, 275, respectively. A person loses one 454gms of weight for each 3500
calories burned. Write a python program that requires the user to input the
number of hours spent at each activity and then calculates the number of
kilograms worked off.
"""


def calculate_weight_loss(bicycling_hours, jogging_hours, swimming_hours):
    # Calories burned per hour for each activity
    calories_bicycling = 200
    calories_jog = 475
    calories_swimming = 275

    # Total calories burned
    total_calories = (bicycling_hours * calories_bicycling) + (jogging_hours *
                                                               calories_jog) +\
                     (swimming_hours * calories_swimming)

    # Calculate weight loss in kilograms
    weight_loss_kg = (total_calories / 3500) * 454 / 1000  # Convert g to kg

    return weight_loss_kg


def main():
    # Input hours spent at each activity
    bicycling_hours = float(input("Enter the number of hours spent "
                                  "bicycling: "))
    jogging_hours = float(input("Enter the number of hours spent "
                                "jogging: "))
    swimming_hours = float(input("Enter the number of hours spent swimming: "))

    # Calculate weight loss
    weight_loss = calculate_weight_loss(bicycling_hours, jogging_hours,
                                        swimming_hours)

    # Display the result
    print("You worked off {:.2f} kilograms.".format(weight_loss))


if __name__ == "__main__":
    main()

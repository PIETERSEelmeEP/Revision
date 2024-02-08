"""The numbers of calories burned per hour by bicycling, jogging, swimming are
200, 475, 275, respectively. A person loses one 454gms of weight for each 3500
calories burned. Write a python program that requires the user to input the
number of hours spent at each activity and then calculates the number of
kilograms worked off.
"""


def main():
    calories_per_hour = {'bicycling': 200, 'jogging': 475, 'swimming': 275}
    hours_spent = {activity: float(input(f"Enter hours spent {activity}: "))
                   for activity in calories_per_hour}
    total_calories = sum(hours * calories_per_hour[activity] for activity,
                         hours in hours_spent.items())
    kilograms_lost = total_calories / 3500
    print(f"You worked off {kilograms_lost:.2f} kilograms.")


if __name__ == "__main__":
    main()

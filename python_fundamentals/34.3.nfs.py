number_of_cars = int(input())

cars_dictionary = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars_dictionary[car] = {"mileage":int(mileage), "fuel":int(fuel)}

# print(cars_dictionary.items())

while True:
    command = input()

    if command == "Stop":
        for car in cars_dictionary.keys():
            mileage = cars_dictionary[car]["mileage"]
            fuel = cars_dictionary[car]["fuel"]
            print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
        break

    command_list = command.split(" : ")

    if "Drive" in command:
        auto = command_list[1]
        distance = int(command_list[2])
        consumed_fuel = int(command_list[3])
        if cars_dictionary[auto]["fuel"] >= consumed_fuel:
            cars_dictionary[auto]["mileage"] += distance
            cars_dictionary[auto]["fuel"] -= consumed_fuel
            print(f"{auto} driven for {distance} kilometers. {consumed_fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if cars_dictionary[auto]["mileage"] >= 100000:
            print(f"Time to sell the {auto}!")
            cars_dictionary.pop(auto)

    if "Refuel" in command:
        auto = command_list[1]
        refilled_fuel = int(command_list[2])
        current_fuel = cars_dictionary[auto]["fuel"]
        if (current_fuel + refilled_fuel) > 75:
            print(f"{auto} refueled with {(75 - current_fuel)} liters")
            cars_dictionary[auto]["fuel"] = 75
        else:
            print(f"{auto} refueled with {refilled_fuel} liters")
            cars_dictionary[auto]["fuel"] += refilled_fuel

    if "Revert" in command:
        auto = command_list[1]
        kilometers = int(command_list[2])
        current_kms = cars_dictionary[auto]["mileage"]
        if (current_kms - kilometers) < 10000:
            cars_dictionary[auto]["mileage"] = 10000
        else:
            cars_dictionary[auto]["mileage"] -= kilometers
            print(f"{auto} mileage decreased by {kilometers} kilometers")
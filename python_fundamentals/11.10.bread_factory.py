day_list = input().split("|")
# print(day_list)

energy = 100
coins = 100

for each in day_list:
    case, number = each.split("-")
    number = int(number)
    # print(case)
    # print(number)

    if case == "rest":
        if energy + number >= 100:
            current_energy = 100
            print(f"You gained {100 - energy} energy.")
            print(f"Current energy: {current_energy}.")
            energy = current_energy
        else:
            energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {energy}.")

    elif case == "order":

        if energy - 30 >= 0:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins - number >= 0:
            coins -= number
            print(f"You bought {case}.")
        else:
            print(f"Closed! Cannot afford {case}." )
            break

else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
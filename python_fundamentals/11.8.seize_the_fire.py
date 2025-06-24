# getting all fires information in one string, each fire's info separated by #
all_fires_info = input()

# amount of water for putting out the fire
water = int(input())

# parsing the string into a list with each fire's info stored as a separate string item
all_fires_list = all_fires_info.split("#")

cells_put = []
effort = 0
total_fire = 0

current_fire = []

#parsing each item in the all_fires_list
for each in range(len(all_fires_list)):

    # turning each fire info into a smaller list for easier parsing, checking if the cell value is within the fire's range
    # if yes, then checking if we have enough water
    # and if we have, we append this value to the list with put fires (cells_put) and recalculate the water, effort and total_fire

    if "High" in all_fires_list[each]:
        current_fire = all_fires_list[each].split(" = ")

        if 81 <= int(current_fire[1]) <= 125:

            if int(current_fire[1]) <= water:
                cells_put.append(int(current_fire[1]))
                water -= int(current_fire[1])
                effort += int(current_fire[1]) * 0.25
                total_fire += int(current_fire[1])


    if "Medium" in all_fires_list[each]:
        current_fire = all_fires_list[each].split(" = ")

        if 51 <= int(current_fire[1]) <= 80:

            if int(current_fire[1]) <= water:
                cells_put.append(int(current_fire[1]))
                water -= int(current_fire[1])
                effort += int(current_fire[1]) * 0.25
                total_fire += int(current_fire[1])


    if "Low" in all_fires_list[each]:
        current_fire = all_fires_list[each].split(" = ")

        if 1 <= int(current_fire[1]) <= 50:

            if int(current_fire[1]) <= water:
                cells_put.append(int(current_fire[1]))
                water -= int(current_fire[1])
                effort += int(current_fire[1]) * 0.25
                total_fire += int(current_fire[1])


print("Cells:")

for cell in range(len(cells_put)):
    print(f" - {cells_put[cell]}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
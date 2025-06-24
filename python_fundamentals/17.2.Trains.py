number = int(input())

wagons = [0] * number

while True:
    command = input()
    command_list = command.split()
    if command == "End":
        print(wagons)
        break
    elif "add" in command_list:
        wagons[-1] += int(command_list[1])
    elif "insert" in command_list:
        wagons[int(command_list[1])] += int(command_list[2])
    elif "leave" in command_list:
        wagons[int(command_list[1])] -= int(command_list[2])

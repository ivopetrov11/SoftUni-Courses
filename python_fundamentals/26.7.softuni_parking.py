number_of_commands = int(input())

registry_dictionary = {}

for _ in range(number_of_commands):
    command_list = input().split()
    command = command_list[0]
    name = command_list[1]

    if command == "register":
        if name not in registry_dictionary.keys():
            plate = command_list[2]
            registry_dictionary[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {registry_dictionary[name]}")
    elif command == "unregister":
        if name not in registry_dictionary.keys():
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            registry_dictionary.pop(name)

for username, license_plate_number in registry_dictionary.items():
    print(f"{username} => {license_plate_number}")

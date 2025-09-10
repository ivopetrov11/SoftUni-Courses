commands = input().lower()
commands_list = commands.split()
commands_dictionary = {}
# print(commands_list)

for command in commands_list:
    if command not in commands_dictionary.keys():
        commands_dictionary[command] = 0
    commands_dictionary[command] += 1

# print(commands_dictionary)

for key, value in commands_dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
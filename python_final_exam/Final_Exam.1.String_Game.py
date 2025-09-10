string_input = input()

while True:
    command = input()

    if command == "Done":

        break


    command_list = command.split()

    if "Change" in command:
        current_char = command_list[1]
        new_char = command_list[2]
        for each_char in string_input:
            if each_char == current_char:
                string_input = string_input.replace(current_char,new_char)
        print(string_input)

    if "Includes" in command:
        substring = command_list[1]
        if substring in string_input:
            print("True")
        else:
            print("False")

    if "End" in command:
        substring = command_list[1]
        if string_input.endswith(substring):
            print("True")
        else:
            print("False")

    if "Uppercase" in command:
        string_input = string_input.upper()
        print(string_input)

    if "FindIndex" in command:
        char = command_list[1]
        print(string_input.index(char))

    if "Cut" in command:
        startIndex = int(command_list[1])
        finalIndex = startIndex + int(command_list[2])
        string_input = string_input[startIndex:finalIndex]
        print(string_input)
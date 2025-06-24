strings_list = input().split()

output_string = ""
current_output_list = []

while True:
    # commands are entered until "end" command is received
    command = input()

    # check if command is for end, if not -> continues
    if command == "3:1":
        # formats the output
        print(f"{' '.join(map(str,strings_list))}")
        break

    # splitting the command string into a list of elements
    command_list = command.split(" ")

    # temp storage variables - reset with each iteration
    current_string = ""
    current_list = []

    if command_list[0] == "merge":
        # making sure that whatever numbers are input as start and end indices, they will be represented in the range of indices of the command_list
        start_index = max(0, min(int(command_list[1]), len(strings_list) - 1))
        end_index = max(0, min(int(command_list[2]), len(strings_list) - 1))

        # print(f"Part selected -> {strings_list[start_index: end_index + 1]}") # DEBUG PRINT

        # each item in the selection of the list is added to current_string and to current_list
        for each in strings_list[start_index: end_index +1]:
            current_string += str(each)
            current_list.append(each)

        # strings_list now gets only the items that were out of the selection
        strings_list = [word for word in strings_list if word not in current_list]

        #inserting the selection on the start_index place thereby creating the image of replacement
        strings_list.insert(start_index, current_string)

        # print(f"Output so far -> {strings_list}") # DEBUG PRINT

    if command_list[0] == "divide":

        index = int(command_list[1])
        target = strings_list[index]  # the targeted string

        # number of partitions i.e. the number of parts for the targeted string to be divided
        partitions = int(command_list[2])

        # calculating the length of each part that is to be divided
        partitions_length = len(target) // partitions

        count_index = 0

        for iter_index in range(partitions):
            # when we get to the last iteration, we append to the current_list temp variable
            # what is left from the targeted string
            if iter_index == partitions - 1:
                current_list.append(target[count_index:])

            # until we reach the final iteration, we append parts of the targeted string to the current_list variable
            # and increase the count_index with the partition_length number -> serves as a step
            else:
                # each partition from the targeted string takes count_index as a start and the partition_length as number of chars to include
                current_list.append(target[count_index: count_index + partitions_length])
                count_index += partitions_length

        strings_list[index:index + 1] = current_list
        # print(strings_list) # DEBUG PRINT
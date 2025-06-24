gifts = input()

#receiving initial command
command = input()

#gifts are input as a whole string - they are to be split by " " and turned into a list
gifts_list =  gifts.split(" ")

#declaring empty list that will serve for as a storage of the values for the final output
final_list = []


while command != "No Money":

    # as long as the command is "No Money", each command input is parsed into a list in its own case
    # then the attributes are accessed by index, if the index is valid; if it's not -> then the loop continues
    if "Required" in command:
        command_as_list = command.split(" ")
        index = int(command_as_list[2])
        if 0 <= index < len(gifts_list):
            gifts_list[index] = command_as_list[1]
    if "JustInCase" in command:
        command_as_list = command.split(" ")
        gifts_list[-1] = command_as_list[1]
    if "OutOfStock" in command:
        command_as_list = command.split(" ")
        while command_as_list[1] in gifts_list:
            index = gifts_list.index(command_as_list[1])
            gifts_list[index] = "None"
    command = input()

else:
    # [OUTDATED] excluding "None" values from the list after all commands, right before output
    # [OUTDATED]  while "None" in gifts_list:
    # [OUTDATED]      gifts_list.remove("None")

    # iterating all the items in the gifts_list and adding to the final_list only the ones which are not "None"
    for item in gifts_list:
        if item != "None":
            final_list.append(item)
        
    # transforming the list into a tuple to add the spacing between the values and output them correctly
    gifts_tuple = tuple(final_list)
    output = " ".join(gifts_tuple)
    print(output)
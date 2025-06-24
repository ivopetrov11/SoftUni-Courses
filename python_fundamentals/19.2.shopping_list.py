shopping_list = input().split("!")

while True:
    command = input()

    if command == "Go Shopping!":
        # print(shopping_list)
        print(f"{', '.join(map(str, shopping_list))}")
        break

    command_list = command.split(" ")

    if "Urgent" in command_list:
        item = command_list[1]
        if item not in shopping_list:
            shopping_list.insert(0,item)
        else:
            continue

    if "Unnecessary" in command_list:
        item = command_list[1]
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            continue

    if "Correct" in command_list:
        old_item = command_list[1]
        if old_item in shopping_list:
            new_item = command_list[2]
            old_idx = shopping_list.index(old_item)
            shopping_list[old_idx] = new_item
        else:
            continue

    if "Rearrange" in command_list:
        item = command_list[1]
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)
        else:
            continue
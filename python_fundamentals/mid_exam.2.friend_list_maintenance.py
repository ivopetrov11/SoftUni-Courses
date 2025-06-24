friends_list = input().split(", ")
blacklisted = 0
lost = 0

def index_validation(lst:list, n:int):
    return n in range (0, len(lst))

while True:
    command = input()

    if command == "Report":
        print(f"Blacklisted names: {blacklisted}")
        print(f"Lost names: {lost}")
        print(f"{' '.join(map(str, friends_list))}")
        break

    command_list = command.split()

    if "Blacklist" in command_list:
        name = command_list[1]
        if name in friends_list:
            print(f"{name} was blacklisted.")
            name_idx = friends_list.index(name)
            friends_list[name_idx] = "Blacklisted"
            blacklisted += 1
        else:
            print(f"{name} was not found.")
        # print(friends_list) # DEBUG PRINT

    if "Error" in command_list:
        index = int(command_list[1])

        if index_validation(friends_list, index):
            friend = friends_list[index]

            if friend == "Blacklisted" or friend == "Lost":
                continue
            else:
                print(f"{friend} was lost due to an error.")
                friends_list[index] = "Lost"
                lost += 1
        else:
            continue
#         print(friends_list)  # DEBUG PRINT

    if "Change" in command_list:
        index = int(command_list[1])

        if index_validation(friends_list, index):
            new_name = command_list[2]
            print(f"{friends_list[index]} changed his username to {new_name}.")
            friends_list[index] = new_name
        else:
            continue

#         print(friends_list) # DEBUG PRINT
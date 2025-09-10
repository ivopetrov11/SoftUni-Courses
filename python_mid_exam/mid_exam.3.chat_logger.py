chat_list = []

while True:
    command = input()

    if command == "end":
        for each in chat_list:
            print(each)
        break

    command_list = command.split()

    if "Chat" in command_list:
        message = command_list[1]
        chat_list.append(message)
        # print(chat_list) # DEBUG PRINT

    if "Delete" in command_list:
        message = command_list[1]

        if message in chat_list:
            chat_list.remove(message)
        else:
            continue

#         print(chat_list) # DEBUG PRINT

    if "Edit" in command_list:
        message = command_list[1]

        if message in chat_list:
            msg_idx = chat_list.index(message)
            edit = command_list[2]
            chat_list[msg_idx] = edit
        else:
            continue

#         print(chat_list) # DEBUG PRINT

    if "Pin" in command_list:
        message = command_list[1]

#         print(f"Before Pin: {chat_list}") # DEBUG PRINT

        if message in chat_list:
#             print(message) # DEBUG PRINT
            msg_idx = chat_list.index(message)
            pin = chat_list.pop(msg_idx)
#             print(f"Before swap: {chat_list}") # DEBUG PRINT
            chat_list.append(pin)
#             print(f"After swap: {chat_list}") # DEBUG PRINT
        else:
            continue

#         print(chat_list) # DEBUG PRINT

    if "Spam" in command_list:
        for message in command_list:
            if message != "Spam":
                chat_list.append(message)
            else:
                pass

#         print(chat_list) # DEBUG PRINT

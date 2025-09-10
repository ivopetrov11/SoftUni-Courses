messages_limit = int(input())

users_dictionary = {}

while True:
    command = input()

    if command == "Statistics":
        users_left = len(users_dictionary.keys())
        print(f"Users count: {users_left}")
        for each_user in users_dictionary.keys():
            all_messages = users_dictionary[each_user]["sent"] + users_dictionary[each_user]["received"]
            print(f"{each_user} - {all_messages}")
        break

    command_list = command.split("=")

    if "Add" in command:
        username = command_list[1]

        if username not in users_dictionary.keys():
            sent = int(command_list[2])
            received = int(command_list[3])
            users_dictionary[username] = {"sent":sent, "received":received}

    if "Message" in command:
        sender = command_list[1]
        receiver = command_list[2]
        if sender in users_dictionary.keys() and receiver in users_dictionary.keys():
            users_dictionary[sender]["sent"] += 1
            users_dictionary[receiver]["received"] += 1
            sender_check = users_dictionary[sender]["sent"] + users_dictionary[sender]["received"]
            receiver_check = users_dictionary[receiver]["received"] + users_dictionary[receiver]["sent"]
            if sender_check >= messages_limit:
                print(f"{sender} reached the capacity!")
                users_dictionary.pop(sender)
            if receiver_check >= messages_limit:
                print(f"{receiver} reached the capacity!")
                users_dictionary.pop(receiver)

    if "Empty" in command:
        user = command_list[1]
        if user == "All":
            users_dictionary.clear()
        else:
            if user in users_dictionary.keys():
                users_dictionary.pop(user)
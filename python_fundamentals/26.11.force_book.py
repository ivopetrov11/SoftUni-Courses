force_dictionary = {} # keys -> force_side, values -> force_user lists


while True:

    info = input()

    if info == "Lumpawaroo":
        for side, members in force_dictionary.items():
            if len(members) > 0:
                print(f"Side: {side}, Members: {len(members)}")
                for each_member in members:
                    print(f"! {each_member}")
        break

    force_user_already_exists = False

    if "|" in info:
        force_side, force_user = info.split(" | ")      # "{force_side} | {force_user}"

        for user_list in force_dictionary.values():
            if force_user in user_list:
                force_user_already_exists = True

        if force_side not in force_dictionary.keys():
            force_dictionary[force_side] = []

        if not force_user_already_exists:
            force_dictionary[force_side].append(force_user)



    if "->" in info:
        force_user, force_side = info.split(" -> ")         # "{force_user} -> {force_side}"

        joins_new_force = False

        if force_side not in force_dictionary.keys():
            force_dictionary[force_side] = []

        for current_force, user_list in force_dictionary.items():
            if force_user in user_list:
                force_user_already_exists = True
                if current_force != force_side:
                    force_dictionary[current_force].remove(force_user)
                    force_dictionary[force_side].append(force_user)
                    joins_new_force = True
                    break

        if not force_user_already_exists:
            force_dictionary[force_side].append(force_user)
            joins_new_force = True

        if joins_new_force:
            print(f"{force_user} joins the {force_side} side!")

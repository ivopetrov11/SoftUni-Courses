courses_list = input().split(", ")

while True:
    command = input()

    if command == "course start":
        # print(courses_list)
        for place in range(1, len(courses_list) + 1):
            # print(f"{f'{place} '.join(map(str, courses_list))}")
            print(f"{place}.{courses_list[place-1]}")
        break

    command_list = command.split(":")

    if "Add" in command_list:
        lesson_title = command_list[1]
        if lesson_title not in courses_list:
            courses_list.append(lesson_title)
        # print(courses_list)

    if "Insert" in command_list:
        lesson_title = command_list[1]
        index = int(command_list[2])
        if lesson_title not in courses_list:
            courses_list.insert(index,lesson_title)
#         print(courses_list)

    if "Remove" in command_list:
        lesson_title = command_list[1]
        if lesson_title in courses_list:
            if f"{lesson_title}-Exercise" in courses_list:
                courses_list.remove(f"{lesson_title}-Exercise")

            courses_list.remove(lesson_title)
#         print(courses_list)

    if "Swap" in command_list:
        first_title = command_list[1]
        second_title = command_list[2]

        if first_title in courses_list and second_title in courses_list:
            first_idx = courses_list.index(first_title)
            second_idx = courses_list.index(second_title)
            courses_list[first_idx], courses_list[second_idx] = courses_list[second_idx], courses_list[first_idx]
#             print(courses_list)

            if f"{first_title}-Exercise" in courses_list:
                first_ex_idx = courses_list.index(f"{first_title}-Exercise")
                courses_list.pop(first_ex_idx)
                courses_list.insert(first_idx + 1, f"{first_title}-Exercise")
#                 print(courses_list)

            if f"{second_title}-Exercise" in courses_list:
                second_ex_idx = courses_list.index(f"{second_title}-Exercise")
                courses_list.pop(second_ex_idx)
                courses_list.insert(courses_list.index(second_title) + 1, f"{second_title}-Exercise")
                # print(courses_list)
#

    if "Exercise" in command_list:
        lesson_title = command_list[1]
        if lesson_title in courses_list and f"{lesson_title}-Exercise" not in courses_list:
            lesson_idx = courses_list.index(lesson_title)
            courses_list.insert(lesson_idx + 1, f"{lesson_title}-Exercise")
            # print(courses_list)
        elif lesson_title not in courses_list:
            courses_list.append(lesson_title)
            courses_list.append(f"{lesson_title}-Exercise")
            # print(courses_list)




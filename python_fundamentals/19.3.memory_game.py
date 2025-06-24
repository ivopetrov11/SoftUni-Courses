sequence_list = input().split()
moves = 0

# index validation check
def valid_index(lst: list, n: int):
    return n in range(len(lst))

while sequence_list:
    command = input()
    moves += 1

    if command == "end" and sequence_list:
        print(f"Sorry you lose :( \n{' '.join(map(str, sequence_list))}")
        # print(sequence_list) # DEBUG PRINT
        break

    command_list = command.split(" ")
    idx_1 = int(command_list[0])
    idx_2 = int(command_list[1])
    # idx_1 = int(idx_1)
    # idx_2 = int(idx_2)

    # if idx_1 == idx_2 or idx_1 < 0 or idx_2 < 0 or idx_1 > len(sequence_list) - 1 or idx_2 > len(sequence_list) - 1:
    if idx_1 == idx_2 or not valid_index(sequence_list, idx_1) or not valid_index(sequence_list, idx_2):

        twin_1 = "-"+str(moves)+"a"
        twin_2 = "-" + str(moves) + "a"

        # insert_index = int((len(sequence_list)) / 2)
        insert_index = len(sequence_list) // 2
        sequence_list.insert(insert_index,twin_1)
        insert_index = len(sequence_list) // 2
        sequence_list.insert(insert_index, twin_2)

        print("Invalid input! Adding additional elements to the board")
#         print(sequence_list) # DEBUG PRINT

    elif sequence_list[idx_1] == sequence_list[idx_2]:
        print(f"Congrats! You have found matching elements - {sequence_list[idx_2]}!")
        temp_list = [each for each in sequence_list if each != sequence_list[idx_2]]
        sequence_list = temp_list
        # print(sequence_list) # DEBUG PRINT
    elif sequence_list[idx_1] != sequence_list[idx_2]:
        print("Try again!")
#         print(sequence_list) # DEBUG PRINT

else:
    print(f"You have won in {moves} turns!")
#     print(sequence_list) # DEBUG PRINT


    # elif command == "end" and not sequence_list:
    #     print(f"You have won in {moves} turns!")
    #     # print(sequence_list) # DEBUG PRINT
    #     break
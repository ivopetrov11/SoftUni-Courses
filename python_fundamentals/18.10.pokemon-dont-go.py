integers_list = [int(each) for each in input().split()]
# print(integers_list)
sum_captured = 0
step = 0

while integers_list:
    step += 1
    index_input = int(input())
    # print(integers_list)

    if 0 <= index_input < len(integers_list):
        captured = integers_list.pop(index_input)
        sum_captured += captured
        current_list = []

        for number in integers_list:
            if captured >= number:
                number += captured
                current_list.append(number)
            elif captured < number:
                number -= captured
                current_list.append(number)

        integers_list = current_list

        # DEBUG PRINT
        # print(f"Step {step}: \n Result: {sum_captured} \n List: {integers_list}")

    elif index_input < 0:
        captured = integers_list[0]
        sum_captured += captured
        integers_list[0] = integers_list[-1]

        current_list = []

        for number in integers_list:
            if captured >= number:
                number += captured
                current_list.append(number)
            elif captured < number:
                number -= captured
                current_list.append(number)

        integers_list = current_list

        # DEBUG PRINT
        # print(f"Step {step}: \nResult: {sum_captured} \nList: {integers_list} \n")

    elif index_input > len(integers_list)-1:
        captured = integers_list[-1]
        sum_captured += captured
        integers_list[-1] = integers_list[0]

        current_list = []

        for number in integers_list:
            if captured >= number:
                number += captured
                current_list.append(number)
            elif captured < number:
                number -= captured
                current_list.append(number)

        integers_list = current_list

        # DEBUG PRINT
        # print(f"Step {step}: \n Result: {sum_captured} \n List: {integers_list}")

print(sum_captured)






# def increase_decrease(index:int, lst: list):
#     sum_captured = 0
#
#     if 0 <= index < len(lst):
#         captured = lst.pop(index)
#
#         sum_captured += captured
#         temp_list = []
#
#         for each in lst:
#             if captured >= each:
#                 each += captured
#                 temp_list.append(each)
#             elif captured < each:
#                 each -= captured
#                 temp_list.append(each)
#
#         lst = temp_list
#
#     elif index < 0:
#         captured = integers_list[0]
#         sum_captured += captured
#         lst[0] = lst[-1]
#
#         temp_list = []
#
#         for each in lst:
#             if captured >= each:
#                 each += captured
#                 temp_list.append(each)
#             elif captured < each:
#                 each -= captured
#                 temp_list.append(each)
#
#         lst = temp_list
#
#     elif index > 0:
#         captured = integers_list[-1]
#         sum_captured += captured
#         lst[-1] = lst[0]
#
#         temp_list = []
#
#         for each in lst:
#             if captured >= each:
#                 each += captured
#                 temp_list.append(each)
#             elif captured < each:
#                 each -= captured
#                 temp_list.append(each)
#
#         lst = temp_list
#
#     return sum_captured


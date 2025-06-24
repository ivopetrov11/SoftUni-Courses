string_list = input().split(", ")
numbers_list = [int(each) for each in string_list]

# SOLUTION FROM THE EXERCISE LECTURE
group = 10

while len(numbers_list) > 0:
    output_list = [num for num in numbers_list if num <= group]
    print(f" Group of {group}'s: {output_list}")
    numbers_list = [num for num in numbers_list if num not in output_list]
    group += 10

# THE SOLUTION BELOW DOES NOT PASS ALL TEST IN JUDGE - 60/100
# def sorting(lst: list):
#     prev_group = 0
#     group = 10
#     for each in lst:
#         output_list = [num for num in lst if prev_group < num <= group]
#         print(f" Group of {group}'s: {output_list}")
#         prev_group = group
#         group += 10
#         if group - max(lst) > 9:
#             break
#
# sorting(numbers_list)
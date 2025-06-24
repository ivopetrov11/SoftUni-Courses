numbers_list = input().split(", ")
indices_list = [int(index) for index in range(len(numbers_list)) if int(numbers_list[index]) % 2 == 0]

print(indices_list)
# def even_numbers(lst: list):
#     """getting the indices of even numbers"""
#     indices_list = [int(index) for index in range(len(lst)) if int(lst[index]) % 2 == 0]
#     return indices_list


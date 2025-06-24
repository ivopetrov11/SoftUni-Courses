number_string = input()
number_string_list = number_string.split()
number_int_list = [int(each) for each in number_string_list]

def even_numbers(num: int) -> bool:
    return num % 2 == 0


result = list(filter(even_numbers,number_int_list))
print(result)

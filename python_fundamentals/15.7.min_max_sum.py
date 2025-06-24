number_string = input()
number_string_list = [int(num) for num in number_string.split()]

# print(number_string_list)

print(f"The minimum number is {min(number_string_list)}")
print(f"The maximum number is {max(number_string_list)}")
print(f"The sum number is: {sum(number_string_list)}")

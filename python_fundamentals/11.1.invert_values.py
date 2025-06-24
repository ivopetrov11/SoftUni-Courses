numbers_string = input()
numbers_list = numbers_string.split(" ")
filtered_list = []

for index in range(0, len(numbers_list)):
    number_int = -int(numbers_list[index])
    filtered_list.append(number_int)

print(filtered_list)
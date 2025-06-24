numbers_string = input()
count_removed = int(input())

numbers_list_strings = numbers_string.split(" ")
numbers_list_int = []

#turning each element in the list from str to int to be able to use the min method later
for each in range(len(numbers_list_strings)):
    number_int = int(numbers_list_strings[each])
    numbers_list_int.append(number_int)

#for-loop remove each min element left
for time in range(count_removed):
    numbers_list_int.remove(min(numbers_list_int))

#clearing the list where numbers were stored as strings to use it for the new number sequence without min values
numbers_list_strings = []

#turning each int number in the list back into str to add ", " in the final output
for each_item in range(len(numbers_list_int)):
    number_str = str(numbers_list_int[each_item])
    numbers_list_strings.append(number_str)

#assigning a tuple that accepts all values from the new numbers list where numbers are stored as strings
number_tuple = tuple(numbers_list_strings)
output = ", ".join(number_tuple)
print(output)
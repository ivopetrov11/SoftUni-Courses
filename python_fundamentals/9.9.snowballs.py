# saving the results into a string (list) or maybe a dictionary???

number = int(input())
value = 0
weight_dict = {}
time_dict = {}
quality_dict = {}
value_dict = {}

value_list = []

for index in range(number):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight // time_needed) ** quality

# update each dictionary for each value every time there is an input
    weight_dict.update({index : weight})
    time_dict.update({index : time_needed})
    quality_dict.update({index : quality})
    value_dict.update({index : value})

    print(f"{weight} : {time_needed} = {value} ({quality})")


# call values from value_dict, take the max() one and its index
# call the other vars - weight, time and quality by that index

# NO NEED FOR DICTIONARIES, BECAUSE WE DON'T NEED TO SAVE ALL THE INFO
# ESTABLISH ONLY MAX_VARIABLES FOR EACH PARAMETER AND IF CURRENT_VALUE > VALUE, THEN VALUE = CURRENT_VALUE, MAX_WEIGHT = CURRENT_WEIGHT ETC.

for values in value_dict.values():
    value_to_int = int(values)
    value_list.append(value_to_int)

    print (values)

max_value = max(value_list)

for search_value in value_dict.values():
    if max_value == search_value:
        print(value_dict.keys())
        #print(value_dict.get(max_value))

print(weight_dict)
print(time_dict)
print(quality_dict)
print(value_dict)

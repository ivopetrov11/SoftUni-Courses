first_sequence_list = input().split(", ")
second_sequence_list = input().split(", ")

output_list = []

for each in first_sequence_list:
    for item in second_sequence_list:
        if each in item:
            if each not in output_list:
                output_list.append(each)

print(output_list)
info_list = input().split()
output_string = ""
for each in info_list:
    output_string += (each * len(each))

print(output_string)
input_list = input().split(">")
strength = 0
output_list = []

for string in input_list:

    contains_explosion_number = False

    if string[0].isnumeric():
        strength += int(string[0])
        contains_explosion_number = True

    if contains_explosion_number:
        if strength >= len(string):
            strength -= len(string)
            string = ""
            output_list.append(string)
        else:
            string = string[strength:]
            output_list.append(string)
            strength = 0

    else:
        output_list.append(string)


print('>'.join(each for each in output_list))



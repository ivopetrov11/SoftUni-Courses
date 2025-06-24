string1 = input()
string2 = input()
last_printed = string1


for char_index in range (len(string1)):
    left_side = string2[:char_index+1]
    right_side = string1[char_index+1:]
    new_string = left_side + right_side
    if new_string != last_printed:
        print(new_string)
        last_printed = new_string
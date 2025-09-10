strings_list = input().split()
total_result = 0

for string in strings_list:
    current_string = string.strip()

    # if uppercase -> letter_num = ord(string[0]) - 64
    # if lowercase -> letter_num = ord(string[0]) - 96

    first_letter_num = 0
    last_letter_num = 0
    first_letter_up = False
    last_letter_up = False

    current_result = int(current_string[1:-1])

    if current_string[0].isupper():
        first_letter_num = ord(current_string[0]) - 64
        first_letter_up = True

    if current_string[0].islower():
        first_letter_num = ord(current_string[0]) - 96
        first_letter_up = False

    if current_string[-1].isupper():
        last_letter_num = ord(current_string[-1]) - 64
        last_letter_up = True

    if current_string[-1].islower():
        last_letter_num = ord(current_string[-1]) - 96
        last_letter_up = False


    if first_letter_up:
        current_result = current_result / first_letter_num

    elif not first_letter_up:
        current_result = current_result * first_letter_num


    if last_letter_up:
        current_result = current_result - last_letter_num

    elif not last_letter_up:
        current_result = current_result + last_letter_num

    total_result += current_result

print(f"{total_result:.2f}")
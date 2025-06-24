number = int(input())


for current_number in range(1, number + 1):
    current_number_as_string = str(current_number)
    result = 0
    for current_digit in current_number_as_string:
        result += int(current_digit)
    is_special = False
    if result == 5 or result == 7 or result == 11:
        is_special = True
    print(f"{current_number} -> {is_special}")
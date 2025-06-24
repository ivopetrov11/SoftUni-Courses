number_string = input()

def digits_sum (num: str) -> str:
    even_sum = 0
    odd_sum = 0

    for each in num:
        if int(each) % 2 == 0:
            even_sum += int(each)
        elif int(each) % 2 != 0:
            odd_sum += int(each)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


print(digits_sum(number_string))
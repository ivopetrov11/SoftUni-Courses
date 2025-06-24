happiness_string_list = input().split(" ")
factor = int(input())
happiness_int_list = [int(number) for number in happiness_string_list]

def happiness_factor(n):
    return n * factor

#to use map() with factor func
factored_list = list(map(happiness_factor,happiness_int_list))

def happiness_check(lst: list):
    average = sum(lst) / len(lst)
    happy_count = 0
    for each in lst:
        if each >= average:
            happy_count += 1
    if happy_count >= (len(lst) / 2):
       print(f"Score: {happy_count}/{len(lst)}. Employees are happy!")
    else:
        print(f"Score: {happy_count}/{len(lst)}. Employees are not happy!")

happiness_check(factored_list)
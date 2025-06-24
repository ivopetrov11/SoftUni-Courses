# https://www.geeksforgeeks.org/python/print-lists-in-python-4-different-ways/ <- USEFUL FOR LIST PRINTING IN DIFFERENT WAYS

numbers_list = input().split(", ")

#positive
positive_list = [int(each) for each in numbers_list if int(each) >= 0]
print(f"Positive: {', '.join(map(str,positive_list))}")
#negative
negative_list = [int(each) for each in numbers_list if int(each) < 0]
print(f"Negative: {', '.join(map(str,negative_list))}")
#even
even_list = [int(each) for each in numbers_list if int(each) % 2 == 0]
print(f"Even: {', '.join(map(str,even_list))}")
#odd
odd_list = [int(each) for each in numbers_list if int(each) % 2 != 0]
print(f"Odd: {', '.join(map(str,odd_list))}")
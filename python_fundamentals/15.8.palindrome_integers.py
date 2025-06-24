number_string = input()
number_string_list = [num for num in number_string.split(", ")]

# print(number_string_list)

def palindrome(lst:list) -> bool:
    for each in lst:
        if each == each[::-1]:
            print("True")
        else:
            print("False")

palindrome(number_string_list)

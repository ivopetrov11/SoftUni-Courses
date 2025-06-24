strings_list = input().split(" ") #list created from the direct input of strings
search_word = input()

result_count = 0

palindromes_list = [each for each in strings_list if each == each[::-1]]

for word in palindromes_list:
    if word == search_word:
        result_count += 1


print(palindromes_list)
print(f"Found palindrome {result_count} times")

# for each in strings_list:
#     if each == each[::-1]:
#         print(f"{each} is a palindrome")
#     else:
#         print(f"{each} is NOT a palindrome")

# print(strings_list[::-1])
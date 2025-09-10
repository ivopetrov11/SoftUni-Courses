string_input = input()
numbers = ""
letters = ""
others = ""

for each_char in string_input:
    if each_char.isnumeric():
        numbers += each_char
    elif each_char.isalpha():
        letters += each_char
    else:
        others += each_char

print(numbers)
print(letters)
print(others)
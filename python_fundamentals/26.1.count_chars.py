text_input = input()
char_dictionary = {}

for char in text_input:
    if char == " ":
        continue
    if char not in char_dictionary.keys():
        char_dictionary[char] = 0
    char_dictionary[char] += 1

for key, value in char_dictionary.items():
    print(f"{key} -> {value}")
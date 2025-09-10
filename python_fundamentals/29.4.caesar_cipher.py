first_input = input()
final_output = ""

for each_char in first_input:
    final_output += chr(ord(each_char) + 3)

print(final_output)
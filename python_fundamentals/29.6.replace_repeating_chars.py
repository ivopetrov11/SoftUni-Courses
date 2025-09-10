string_input = input()
final_output = string_input[0]

for each_chr in string_input:
    if each_chr != final_output[-1]:
        final_output += each_chr

print(final_output)
# ord() / chr()

number_of_chars = int(input())
char_sum = 0

for char_number in range(number_of_chars):
    char_input = input()
    char_sum += ord(char_input)

print(f"The sum equals: {char_sum}")
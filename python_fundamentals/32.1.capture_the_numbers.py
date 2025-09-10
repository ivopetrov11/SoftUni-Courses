import re

user_input = input()
matches = []

while user_input:

    pattern = r"(\d+)"
    current_matches = re.findall(pattern, user_input)
    matches.extend(current_matches)
    user_input = input()

# print(matches)
for match in matches:
    print(match, end=' ')

import re

user_input = input()
matches = []

while user_input:

    pattern = r"(www\.([A-Za-z\d]+?([-A-Za-z\d]*))\.([a-z]+)?([a-z\.]+))"
    current_matches = re.findall(pattern, user_input)
    matches.extend(current_matches)
    user_input = input()

# print(matches)
for match in matches:
    print(match[0])
import re

user_input = input()

pattern = r"(?<!\_{2})(?<=\_{1})([A-Za-z\d]+)\b"
matches = re.findall(pattern, user_input)
# print(matches)

print(','.join(matches))
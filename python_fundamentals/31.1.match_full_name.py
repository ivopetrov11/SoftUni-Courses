import re
names = input()
regex = r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b"
matches = re.findall(regex, names)
print(' '.join(matches))

# WITH re.findall BUT WHEN HAVING SEPARATE GROUPS
# for match in matches:
#     print(' '.join(match))


# matches = re.finditer(regex, names)
# for match in matches:
#     print(match.group(1))

# matches = re.search(regex, names)
# print(matches.group(1))


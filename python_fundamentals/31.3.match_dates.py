# "dd{separator}MMM{separator}yyyy"

# \b(\d[0-31])([-.\\/])([A-Za-z]{3})\2(\d{4}|)\b

import re
names = input()
regex = r"\b(\d{2})([-./])([A-Za-z]{3})\2(\d{4}|)\b"
matches = re.findall(regex, names)
for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
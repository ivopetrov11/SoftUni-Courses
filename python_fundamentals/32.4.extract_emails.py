# LECTOR's pattern = r"\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
# \s((([A-Za-z\d]+)[A-Za-z\d\.\-\_]*)@([A-Za-z\-]+)(\.[A-Za-z]+)+)\b

import re

sentence = input()
pattern = r"\s((([A-Za-z\d]+)[A-Za-z\d\.\-\_]*)@([A-Za-z\-]+)(\.[A-Za-z]+)+)\b"
matches = re.findall(pattern, sentence)
for email in matches:
    print(email[0])
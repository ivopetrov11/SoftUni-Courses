# 'a', 'o', 'u', 'e', 'i'

text = input()

no_vowels = [symbol for symbol in text if symbol.lower() not in ('a', 'o', 'u', 'e', 'i', ' ') ]

output = str()

for each in no_vowels:
    output += each

print(output)
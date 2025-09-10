import re

user_input = input()
search_word = input()

# pattern = fr"\b(?i){search_word}\b"
pattern = re.compile(fr'\b{search_word}\b',re.IGNORECASE)
matches = re.findall(pattern, user_input)

print(len(matches))
import re

number_of_inputs = int(input())

for _ in range(number_of_inputs):
    boss_is_valid = False
    boss = input()

    pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#"

    validity_check = re.match(pattern, boss)
    if validity_check:
        boss_is_valid = True

    if boss_is_valid:
        valid_boss = re.finditer(pattern, boss)

        for match in valid_boss:
            print(f"{match.group(1)}, The {match.group(2)}")
            print(f">> Strength: {len(match.group(1))}")
            print(f">> Armor: {len(match.group(2))}")
    else:
        print("Access denied!")
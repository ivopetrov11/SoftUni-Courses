import re

pattern = r">>([A-Za-z]+)<<([\d]+[\.]*[\d]+)!(\d+)"

bought_things = []
total_price = 0

while (user_input:=input())!="Purchase":
    matches = re.finditer(pattern, user_input)
    current_price = 0
    current_amount = 0
    for match in matches:
        bought_things.append(match.group(1))
        current_price = float((match.group(2)))
        current_amount = int((match.group(3)))
    total_price += current_price * current_amount

print("Bought furniture:")
for each in bought_things:
    print(each)
print(f"Total money spend: {total_price:.2f}")
lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_shield = 0

expenses = 0

for fights in range (1, lost_fights + 1):

    if fights % 2 == 0:
        expenses += helmet_price
    if fights % 3 == 0:
        expenses += sword_price
        if fights % 2 == 0:
            expenses += shield_price
            broken_shield += 1
            if broken_shield % 2 == 0:
                expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
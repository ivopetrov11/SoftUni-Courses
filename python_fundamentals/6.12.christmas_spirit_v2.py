quantity = int(input())
days_to_xmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

ornament_set_points = 5
tree_skirt_points = 3
tree_garland_points = 10
tree_lights_points = 17

current_cost = 0
current_spirit = 0

for days_counter in range (1, days_to_xmas + 1):
    if days_counter % 11 == 0:
        quantity += 2
    if days_counter % 2 == 0:
        current_cost += ornament_set_price * quantity
        current_spirit += ornament_set_points
    if days_counter % 3 == 0:
        current_cost += (tree_skirt_price + tree_garland_price) * quantity
        current_spirit += (tree_skirt_points + tree_garland_points)
    if days_counter % 5 == 0:
        current_cost += tree_lights_price * quantity
        current_spirit += tree_lights_points
        if days_counter % 3 == 0:
            current_spirit += 30
    if days_counter % 10 == 0:
        current_spirit -= 20
        current_cost += tree_skirt_price + tree_garland_price + tree_lights_price

if days_to_xmas % 10 == 0:
    current_spirit -= 30

total_cost = current_cost
total_spirit = current_spirit
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
quantity = int(input())
days_to_xmas = int(input())

ornament_set_price = 2
ornament_set_points = 5
ornament_set_cost = 0
ornament_set_spirit = 0

tree_skirt_price = 5
tree_skirt_points = 3
tree_skirt_cost = 0
tree_skirt_spirit = 0

tree_garland_price = 3
tree_garland_points = 10
tree_garland_cost = 0
tree_garland_spirit = 0

tree_lights_price = 15
tree_lights_points = 17
tree_lights_cost = 0
tree_lights_spirit = 0

#-----------------------counters-----------------------#
current_cost = 0
current_spirit = 0
#current_quantity = 0

days_counter = 0

days_left = days_to_xmas

# for loop with an if in it representing how much is the cost and the spirit rising/falling on each day
# a day can be both 2nd and 3rd in which case it should do what it does for both
# division checks outside, then check them inside with T/F and do the relevant actions?? - this should be done with a function, so leave it for now??

# second_day = days_counter % 2 == 0
# third_day = days_counter % 3 == 0
# fifth_day = days_counter % 5 == 0
# tenth_day = days_counter % 10 == 0
# eleventh_day = days_counter % 11 == 0

# highest common divisors check?? <- a bit more sophisticated and not for now

for days_counter in range (days_left):
    days_counter += 1

    if days_counter % 2 == 0 and days_counter % 3 == 0 and days_counter % 5 == 0 and days_counter % 10 == 0:
        current_cost += (ornament_set_price + tree_skirt_price + tree_garland_price + tree_lights_price) * quantity
        current_spirit += (ornament_set_points + tree_skirt_points + tree_garland_points +tree_lights_points + 30)
        current_spirit -= 20
        current_cost += tree_skirt_price + tree_garland_price + tree_lights_price

    elif days_counter % 3 == 0 and days_counter % 5 == 0 and days_counter % 10 == 0:
        current_cost += (tree_skirt_price + tree_garland_price + tree_lights_price) * quantity
        current_spirit += (tree_skirt_points + tree_garland_points +tree_lights_points + 30)  # * quantity
        current_spirit -= 20
        current_cost += tree_skirt_price + tree_garland_price + tree_lights_price

    elif days_counter % 2 == 0 and days_counter % 5 == 0 and days_counter % 10 == 0:
        current_cost += (ornament_set_price + tree_lights_price) * quantity
        current_spirit += ornament_set_points + tree_lights_points
        current_spirit -= 20
        current_cost += tree_skirt_price + tree_garland_price + tree_lights_price

    elif days_counter % 2 == 0 and days_counter % 3 == 0 and days_counter % 5 == 0:
        current_cost += (ornament_set_price + tree_skirt_price + tree_garland_price + tree_lights_price) * quantity
        current_spirit += (ornament_set_points + tree_skirt_points + tree_garland_points +tree_lights_points + 30)

    elif days_counter % 2 == 0 and days_counter % 3 == 0:
        current_cost += (tree_skirt_price + tree_garland_price + ornament_set_price) * quantity
        current_spirit += (tree_skirt_points + tree_garland_points +ornament_set_points)
        # tree_skirt_cost += tree_skirt_price * quantity
        # tree_garland_cost += tree_garland_price * quantity
        # ornament_set_cost += ornament_set_price * quantity
        # tree_skirt_spirit += tree_skirt_points
        # tree_garland_spirit += tree_garland_points
        # ornament_set_spirit += ornament_set_points

    elif days_counter % 5 == 0 and days_counter % 10 == 0:
        current_cost += tree_lights_price * quantity
        current_spirit += tree_lights_points
        current_spirit -= 20
        current_cost += tree_skirt_price + tree_garland_price + tree_lights_price
#         tree_lights_cost += tree_lights_price
#         tree_skirt_cost += tree_skirt_price
#         tree_garland_cost += tree_garland_price

    elif days_counter % 2 == 0:
        current_cost += ornament_set_price * quantity
        current_spirit += ornament_set_points #* quantity
#         ornament_set_cost += ornament_set_price * quantity
#         ornament_set_spirit += ornament_set_points
#             print(f"Current cost on each 2nd day : {current_cost}")
#             print(f"Current spirit on each 2nd day : {current_spirit}")
    elif days_counter % 3 == 0:
        current_cost += (tree_skirt_price + tree_garland_price) * quantity
        current_spirit += (tree_skirt_points + tree_garland_points) #* quantity
#         tree_skirt_cost += tree_skirt_price * quantity
#         tree_skirt_spirit += tree_skirt_points
#         tree_garland_cost += tree_garland_price * quantity
#         tree_garland_spirit += tree_garland_points
#             print(f"Current cost on each 3rd day : {current_cost}")
#             print(f"Current spirit on each 3rd day : {current_spirit}")
    elif days_counter % 5 == 0:
        current_cost += tree_lights_price * quantity
        current_spirit += tree_lights_points
#         tree_lights_cost += tree_lights_price * quantity
#         tree_lights_spirit += tree_lights_points
#             print(f"Current cost on each 5th day : {current_cost}")
#             print(f"Current spirit on each 5th day : {current_spirit}")


    # if days_counter % 10 == 0:
    #     current_spirit -= 20
    #     current_cost += tree_skirt_price + tree_garland_price + tree_lights_price
    #     # print(f"Current cost on each 10th day : {current_cost}")
    #     # print(f"Current spirit on each 10th day : {current_spirit}")

    if days_counter % 11 == 0:
        quantity += 2

    if days_counter % 10 == 0 and days_counter == days_left: #days_counter == days left ???
        current_spirit -= 30
#             print(f"Current cost if 10th day is last day : {current_cost}")
#             print(f"Current spirit if 10th day is last day : {current_spirit}")

    print(f"Current cost on day {days_counter} is {current_cost}")
    print(f"Current spirit on day {days_counter} is {current_spirit} \n")
    # print(f"Ornament set so far - cost: {ornament_set_cost} spirit: {ornament_set_spirit}")
    # print(f"Ornament set so far - cost: {tree_skirt_cost} spirit: {tree_skirt_spirit}")
    # print(f"Ornament set so far - cost: {tree_garland_cost} spirit: {tree_garland_spirit}")
    # print(f"Ornament set so far - cost: {tree_lights_cost} spirit: {tree_lights_spirit} \n")

total_cost = current_cost
total_spirit = current_spirit
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")


# while days_left >= 0:
#     # days_left -= 1
#     # days_counter += 1
#     for days_counter in range (days_left):
#         days_left -= 1
#
#         if days_counter % 3 == 0 and days_counter % 5 == 0:
#             current_cost += (tree_skirt_price + tree_garland_price + tree_lights_price) * quantity
#             current_spirit += (tree_skirt_points + tree_garland_points +tree_lights_points + 30)  # * quantity
#             # print(f"Current cost on each 3rd and 5th day : {current_cost}")
#             # print(f"Current spirit on each 3rd and 5th day : {current_spirit}")
#         elif days_counter % 2 == 0:
#             current_cost += ornament_set_price * quantity
#             current_spirit += ornament_set_points #* quantity
# #             print(f"Current cost on each 2nd day : {current_cost}")
# #             print(f"Current spirit on each 2nd day : {current_spirit}")
#         elif days_counter % 3 == 0:
#             current_cost += (tree_skirt_price + tree_garland_price) * quantity
#             current_spirit += (tree_skirt_points + tree_garland_points) #* quantity
# #             print(f"Current cost on each 3rd day : {current_cost}")
# #             print(f"Current spirit on each 3rd day : {current_spirit}")
#         elif days_counter % 5 == 0:
#             current_cost += tree_lights_price * quantity
#             current_spirit += tree_lights_points
# #             print(f"Current cost on each 5th day : {current_cost}")
# #             print(f"Current spirit on each 5th day : {current_spirit}")
#
#         if days_counter % 10 == 0:
#             current_spirit -= 20
#             current_cost += tree_skirt_price + tree_garland_price + tree_lights_price
#             # print(f"Current cost on each 10th day : {current_cost}")
#             # print(f"Current spirit on each 10th day : {current_spirit}")
#
#         if days_counter % 11 == 0:
#             quantity += 2
#
#         if days_counter % 10 == 0 and days_left == 0:
#             current_spirit -= 30
# #             print(f"Current cost if 10th day is last day : {current_cost}")
# #             print(f"Current spirit if 10th day is last day : {current_spirit}")
#
# total_cost = current_cost
# total_spirit = current_spirit
# print(f"Total cost: {total_cost}")
# print(f"Total spirit: {total_spirit}")
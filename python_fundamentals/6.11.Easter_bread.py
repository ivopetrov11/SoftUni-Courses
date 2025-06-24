budget = float(input())
flour_price = float(input())

eggs_price = 0.75 * flour_price
#print(f"Eggs = {eggs_price}")

milk_price = (1.25 * flour_price) / 4
#print(f"Milk = {milk_price}")

one_bread_cost = flour_price + eggs_price + milk_price #recipe
# print(f"1 loaf of bread = {one_bread_cost}")

money_left = budget

                        #counters
current_bread_count = 0
received_eggs = 0
lost_eggs = 0
colored_eggs = 0

while money_left >= one_bread_cost:
    current_bread_count += 1
    received_eggs += 3
    money_left -= one_bread_cost

    if current_bread_count % 3 == 0:
        lost_eggs += current_bread_count - 2

    colored_eggs = received_eggs - lost_eggs

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")














# budget = float(input()) #20
# flour_price = float(input()) #1
#
# eggs_price = 0.75 * flour_price #0.75
# milk_price = (1.25 * flour_price) / 4 #1.25
#
# one_bread_cost = flour_price + eggs_price + milk_price #3  #recipe
# possible_breads = int(budget - (budget % one_bread_cost)) #18
#
# received_eggs = 0
# lost_eggs = 0
# current_bread_count = 0
# # all_bread_cost = 0 #whenever bread is made, its cost is added to this counter; when budget % all_bread_cost < one_bread_cost -> stop making bread
#
# # money_left = budget % all_bread_cost
#
# while budget >= one_bread_cost: #every time a loaf of bread is made, the budget will be reduced with the price of one bread
#     for _ in range(possible_breads):
#         current_bread_count += 1
#         received_eggs += 3
#         budget -= one_bread_cost
#
#         if current_bread_count % 3 == 0:
#             lost_eggs = current_bread_count - 2
#
#         colored_eggs = received_eggs - lost_eggs
#
#     print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
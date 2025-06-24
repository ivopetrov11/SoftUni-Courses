# TO BE SUBMITTED AGAIN AFTER CODE REVIEW
# CODE REVIEW - DONE
# ISSUE WAS WITH USING THE round() function

# getting all items information in one string, each item's info separated by |
items = input()

# budget for buying items
budget = float(input())
if budget < 0:
    exit()

# saving the original budget in this variable, as the original variable will be decreased with each purchase
initial_budget = budget

# parsing the string into a list with each item's info stored as a separate string
items_list = items.split("|")

# dynamic variable for storing the new markup price firstly as a float in the new_prices_float list
# and after the parsing, before output, transform each price as a string
markup_price = 0
new_prices_float = []
new_prices_strings = []

# will use the difference between the original_price_sum and the new_price_sum as a profit
original_price_sum = 0
new_price_sum = 0

current_item = []

# parsing each item in the items_list
for each in range(len(items_list)):

    # turning each item info into a smaller list for easier parsing, checking if the price value is within the item's range
    # if yes, then checking if we have enough budget
    # and if we have, we append this value multiplied by 1.4 (for 40% markup) to the list with new prices (new_prices_float)
    # and recalculate the budget, the original_price_sum and the new_price_sum

    if "Clothes" in items_list[each]:
        current_item = items_list[each].split("->")
        # if current_item[1].isnumeric():
        if 0 <= float(current_item[1]) <= 50:

            if float(current_item[1]) <= budget:
                # markup_price = round(float(current_item[1]) * 1.4, 2)
                markup_price = float(current_item[1]) * 1.4
                new_prices_float.append(markup_price)
                budget -= float(current_item[1])
                new_price_sum += markup_price
                original_price_sum += float(current_item[1])


    if "Shoes" in items_list[each]:
        current_item = items_list[each].split("->")
        # if current_item[1].isnumeric():
        if 0 <= float(current_item[1]) <= 35:

            if float(current_item[1]) <= budget:
                # markup_price = round(float(current_item[1]) * 1.4, 2)
                markup_price = float(current_item[1]) * 1.4
                new_prices_float.append(markup_price)
                budget -= float(current_item[1])
                new_price_sum += markup_price
                original_price_sum += float(current_item[1])


    if "Accessories" in items_list[each]:
        current_item = items_list[each].split("->")
        # if current_item[1].isnumeric():
        if 0 <= float(current_item[1]) <= 20.50:

            if float(current_item[1]) <= budget:
                # markup_price = round(float(current_item[1]) * 1.4, 2)
                markup_price = float(current_item[1]) * 1.4
                new_prices_float.append(markup_price)
                budget -= float(current_item[1])
                new_price_sum += markup_price
                original_price_sum += float(current_item[1])


for price in range(len(new_prices_float)):
    new_prices_strings.append(str(f"{new_prices_float[price]:.2f}"))

price_tuple = tuple(new_prices_strings)
output = " ".join(price_tuple)
print(output)

profit = round((new_price_sum - original_price_sum),2)
print(f"Profit: {profit:.2f}")

if (profit + initial_budget) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

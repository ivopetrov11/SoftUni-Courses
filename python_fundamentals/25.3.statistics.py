# stock = input().split(": ")
# stock_dict = {stock[index]:int(stock[index + 1]) for index in range(0,len(stock),2)}
stock_dict = {}

while (command := input()) != "statistics":
    products = command.split(": ")

    for index in range(0, len(products), 2):
        item, quantity = products[index], products[index +1]
        if item not in stock_dict.keys():
            stock_dict[item] = 0
        stock_dict[item] += int(quantity)

print("Products in stock:")
for product, quantity in stock_dict.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(stock_dict.keys())}")
print(f"Total Quantity: {sum(stock_dict.values())}")


stock = input().split(" ")
stock_dict = {stock[index]:int(stock[index + 1]) for index in range(0,len(stock),2)}
# stock_dict = {}

# for index in range(0, len(stock), 2):
#     food = stock[index]
#     quantity = stock[index + 1]
#     stock_dict[food] = int(quantity)

print(stock_dict)
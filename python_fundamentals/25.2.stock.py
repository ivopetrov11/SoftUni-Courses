stock = input().split()
stock_dict = {stock[index]:int(stock[index + 1]) for index in range(0,len(stock),2)}

products = input().split()

for item in products:
    if item in stock_dict.keys():
        print(f"We have {stock_dict[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
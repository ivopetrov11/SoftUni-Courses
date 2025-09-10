# nested dictionaries
# total price to me formatted to the 2nd decimal digit
products_dictionary = {}

while True:
    info_input = input()
    if info_input == "buy":
        # print(products_dictionary) #DEBUG PRINT
        for stock, info in products_dictionary.items():
            total_price = info["price"]*info["quantity"]
            print(f"{stock} -> {total_price:.2f}")

        break

    info_list = info_input.split()
    product = info_list[0]
    # price = float(info_list[1])
    # quantity = int(info_list[2])

    # if the product does not exist yet, it is created with a value - nested dictionary
    # this nested dictionary stores product information -> price and quantity
    # main key = product, sub keys = "price", "quantity"
    if product not in products_dictionary.keys():
        products_dictionary[product] = {"price":0, "quantity":0}
    products_dictionary[product]["price"] = float(info_list[1])
    products_dictionary[product]["quantity"] += int(info_list[2])
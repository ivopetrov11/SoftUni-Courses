# number_capsules * capsule_price * days = order_price
# Both the price of a coffee and the total price must be formatted to the second decimal plac

order_count = int(input())
order_price = 0
total_price = 0

for _ in range (order_count):
    capsule_price = float(input())
    days = int(input())
    number_capsules = int(input())

    if 0.01 <= capsule_price <= 100 and 1 <= days <= 31 and 1 <= number_capsules <= 2000:
        order_price = number_capsules * capsule_price * days
        print(f"The price for the coffee is: ${order_price:.2f}")
        total_price += order_price
    else:
        continue

print(f"Total: ${total_price:.2f}")
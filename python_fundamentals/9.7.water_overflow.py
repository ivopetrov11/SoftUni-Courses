inputs_number = int(input())
capacity = 255
current_amount = 0

for sip in range(inputs_number):
    pouring = int(input())
    current_amount += pouring
    if current_amount > 255:
        print("Insufficient capacity!")
        current_amount -= pouring

print(current_amount)

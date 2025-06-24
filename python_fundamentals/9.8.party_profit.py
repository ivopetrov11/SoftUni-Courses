group_size = int(input())
days = int(input())
coins = 0

for current_day in range(1, days + 1):
    coins += 50

    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5

    coins -= 2 * group_size

    if current_day % 3 == 0:
        coins -= 3 * group_size
    if current_day % 5 == 0:
        coins += 20 * group_size
        if current_day % 3 == 0:
            coins -= 2 * group_size


    # print(f"Day {current_day}: {group_size} companions; {coins} coins.")

print(f"{group_size} companions received {coins//group_size} coins each.")
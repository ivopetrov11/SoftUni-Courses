plunder_days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

gathered_plunder = 0

for day in range(1, plunder_days +1):

    gathered_plunder += daily_plunder

    if day % 3 == 0:
        gathered_plunder += 0.5 * daily_plunder

    if day % 5 == 0:
        gathered_plunder -= 0.3 * gathered_plunder

if gathered_plunder >= expected_plunder:
    print(f"Ahoy! {gathered_plunder:.2f} plunder gained.")
else:
    percentage = (gathered_plunder / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")

number = int(input())

best_value = 0
best_time = 0
best_quality = 0
best_weight = 0

for index in range(number):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight // current_time) ** current_quality

    if current_value > best_value:
        best_value = current_value
        best_time = current_time
        best_quality = current_quality
        best_weight = current_weight

print(f"{best_weight} : {best_time} = {best_value} ({best_quality})")

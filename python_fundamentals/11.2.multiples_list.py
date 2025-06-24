factor = int(input())
count = int(input())
filtered_list = []

for index in range(1, count + 1):
    current_result = factor * index
    filtered_list.append(current_result)

print(filtered_list)
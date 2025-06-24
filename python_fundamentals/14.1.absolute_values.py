numbers = input().split(" ")

final_output = []

for num in numbers:
    final_output.append(abs(float(num)))

print(final_output)
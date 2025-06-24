divisor = int(input())
boundary = int(input())
max_divisible = 0

for number in range (1,boundary+1):
    if number % divisor == 0:
        max_divisible = number

print(max_divisible)
times = int(input())

positive = []
negative = []

sum_of_negatives = 0

for i in range(times):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)
        sum_of_negatives += number


count_positives = len(positive)
print(positive)
print(negative)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
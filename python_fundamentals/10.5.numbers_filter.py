times = int(input())

positive = []
negative = []
even = []
odd = []
numbers = []
numbers_filtered = []


for i in range(times):
    number = int(input())
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

action = input()

if action == "even":
    print(even)
if action == "odd":
    print(odd)
if action == "negative":
    print(negative)
if action == "positive":
    print(positive)


# numbers = []
# numbers_filtered = []
#
#
# for i in range(times):
#     current_number = int(input())
#
# action = input()
#
# if action == "even":
#     for number in numbers:
#         if number % 2 == 0:
#             numbers_filtered.append(number)
#
# if action == "odd":
#     for number in numbers:
#         if number % 2 != 0:
#             numbers_filtered.append(number)
#
# if action == "negative":
#     for number in numbers:
#         if number < 0:
#             numbers_filtered.append(number)
#
# if action == "positive":
#     for number in numbers:
#         if number >= 0:
#             numbers_filtered.append(number)
#
# print(numbers_filtered)

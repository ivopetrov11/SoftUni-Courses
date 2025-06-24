money_string = input()
beggars_count = int(input())

money_string_list = money_string.split(", ")
money_int_list = []
collected_money_list = []
collected_sum = 0

for index in range(len(money_string_list)):
    money_int = int(money_string_list[index])
    money_int_list.append(money_int)

for beggar in range(beggars_count):
    collected_sum = 0

    for turn in range(beggar , len(money_int_list), beggars_count):
        # print(f"Index {turn} -> {money_int_list[turn]}")
        collected_sum += money_int_list[turn]
#         print(f"Collected : {collected_sum}")
        # turn += 1

    collected_money_list.append(collected_sum)


# print(money_int_list)
print(collected_money_list)
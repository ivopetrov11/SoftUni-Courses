words_list = input().split(" ")
output_list = [each for each in words_list if len(each) % 2 == 0]

for item in output_list:
    print(item)
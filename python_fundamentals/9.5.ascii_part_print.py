start_index = int(input())
end_index = int(input())

for index in range (start_index, end_index + 1):
    char_result = chr(index)
    if index == end_index:
        print(char_result)
    else:
        print(char_result, end=" ")
number = int(input())

# ord(a) = 97

for index in range (97, 97 + number):
    char = chr(index)

    for index2 in range(97, 97 + number):
        char2 = chr(index2)

        for index3 in range(97, 97 + number):
            result_string = ""
            char3 = chr(index3)
            result_string += char + char2 + char3

            print(f"{result_string}")

version_string_list = input().split(".")
version_int_list = [int(each) for each in version_string_list]
# print(version_int_list)

# the check should start from the last number

def version_check(lst: list):
    output_str = str()

    # looping through all list elements backwards
    for each in range(1, len(lst) + 1):
        if lst[-each] != 9:
            lst[-each] += 1
            break
        else:
            lst[-each] = 0

    # adding each list element to the output string
    for i in range(len(lst)):
    # there is a dot added after each number unless the number is the last one (index check)
        if i == len(lst) - 1:
            output_str += str(lst[i])
        else:
            output_str += str(lst[i]) + "."

    print(output_str)

version_check(version_int_list)

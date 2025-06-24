n = int(input())
# prev_codes = []

for _ in range(n):

    code = int(input())

    if code == 88:
        print("Hello")
    elif code == 86:
        print("How are you?")
    elif 86 != code != 88 and code < 88:
        print("GREAT!")
    elif code > 88:
        print("Bye.")
    # elif 86 != code!= 88 and 88 in prev_codes:
    #     print("GREAT!")

    # prev_codes.append(code)

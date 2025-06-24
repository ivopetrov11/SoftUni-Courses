number = int(input())

def loading_bar(num: int) -> str:

    loading_str = "." * 10
    symbol_number = num // 10

    output = loading_str.replace(".","%",symbol_number)

    if symbol_number >= 10:
        print(f"{num}% Complete! \n[{output}]")
    elif 0 <= symbol_number < 10:
        print(f"{num}% [{output}] \nStill loading...")

loading_bar(number)

# loading_str = "." * 10
# output = loading_str.replace(".","%", number//10)
# print(output)
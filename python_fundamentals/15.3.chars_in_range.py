# ord() to be used for getting the ascii code
# chr() to be used to get char from ascii code

char1 = input()
char2 = input()

def symbols_between(ch1: str, chr2: str) -> str:

    result_str = str()
    for symbol in range(ord(ch1)+1, ord(chr2)):
        result_str += chr(symbol)
    return " ".join(result_str)


print(symbols_between(char1,char2))

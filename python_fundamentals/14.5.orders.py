string = input()
counter = int(input())

def order(text: str, count: int):
    if text == "coffee":
        print(f"{count * 1.5:.2f}")
    if text == "water":
        print(f"{count * 1:.2f}")
    if text == "coke":
        print(f"{count * 1.4:.2f}")
    if text == "snacks":
        print(f"{count * 2:.2f}")


order(string, counter)
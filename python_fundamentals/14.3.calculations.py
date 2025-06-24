operator = input()
num1 = int(input())
num2 = int(input())

def operations(op: str, n1: int, n2: int):
    if op == "add":
        print(n1 + n2)
    if op == "subtract":
        print(n1 - n2)
    if op == "multiply":
        print(n1 * n2)
    if op == "divide":
        print(n1 // n2)

operations(operator, num1, num2)
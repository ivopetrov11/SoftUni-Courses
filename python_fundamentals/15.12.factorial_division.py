first_number = int(input())
second_number = int(input())

def factorial(num1: int, num2: int) -> float:
    fact1 = 1
    fact2 = 1
    for each in range(1, num1+1):
        fact1 *= each

    for each in range(1, num2+1):
        fact2 *= each


    result = fact1 / fact2
    print(f"{result:.2f}")


factorial(first_number,second_number)
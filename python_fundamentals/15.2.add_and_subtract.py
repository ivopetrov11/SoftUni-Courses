num1 = int(input())
num2 = int(input())
num3 = int(input())

def sum_numbers(n1: int, n2:int) -> int:
    """returns the summation of two integers"""
    result = n1 + n2
    return result

def subtract(res:int, n3:int) -> int:
    """returns the difference between two integers
    res is for result, reminding that it should take the result of the sum_numbers function
    n3 is the second integer for this function and the third one in general for the program
    the function would return result - n3"""
    return res - n3


print(
    subtract(sum_numbers(num1,num2),num3)
)

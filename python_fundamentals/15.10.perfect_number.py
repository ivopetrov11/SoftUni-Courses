number = int(input())

def aliquot_sum (num: int) -> str:
    divisors_sum = 0
    for each in range(1, num):

        if num % each == 0:
            divisors_sum += each
        #     print(f"Divisor sum: {divisors_sum}")
        # print(f"Divisor: {each} and remainder: {num % each}")

    if divisors_sum == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


aliquot_sum(number)

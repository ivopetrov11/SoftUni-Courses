# to use isalnum() for alphanumeric check
# to use isnum() for number of digits check
from curses.ascii import isalnum

password = input()


def length(word: str):
    if len(word) < 6 or len(word) > 10:
        return False
    return True

def alphanumeric(word: str):
    if not word.isalnum():
        return False
    return True

def digits_sum(word: str):
    digits_num = 0

    for letter in word:
        if letter.isnumeric():
            digits_num += 1

    if digits_num < 2:
        return False
    return True


def validation(word: str):

    if length(word) == True and alphanumeric(word) == True and digits_sum(word) == True:
        print("Password is valid")

    if length(word) == False:
        print("Password must be between 6 and 10 characters")

    if alphanumeric(word) == False:
        print("Password must consist only of letters and digits")

    if digits_sum(word) == False:
        print("Password must have at least 2 digits")

validation(password)



    # digits_num = 0
    #
    # for letter in word:
    #     if letter.isnumeric():
    #         digits_num += 1
    # if len(word) < 6 or len(word) > 10:
    #     print("Password must be between 6 and 10 characters")
    # if not word.isalnum():
    #     print("Password must consist only of letters and digits")
    # if digits_num < 2:
    #     print("Password must have at least 2 digits")
    # else:
    #     print("Password is valid")



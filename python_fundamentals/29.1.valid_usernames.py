usernames_list = input().split(", ")

def length(username: str) -> bool:
    if not (3 <= len(username) <= 16):
        return False
    return True

def content(username: str) -> bool:
    for each_char in username:
        if not (each_char.isalnum() or each_char == "-" or each_char == "_"):
            return False
    return True

def validity(username: str):
    if length(username) and content(username):
        print(username)


for each_input in usernames_list:
    validity(each_input)
def length_is_valid(some_username):
    if 2 < len(some_username) < 17:
        return True
    return False

def content_is_valid(a_username):
    for symbol in a_username:
        if not (symbol.isalnum() or symbol == "_" or symbol == "-"):
            return False
    return True

def no_redundant_symbols(current_username):
    if " " in current_username:
        return False
    return True

def verification_succesful(username):
    if length_is_valid(username) and content_is_valid(username) and no_redundant_symbols(username):
        return True
    return False

usernames = input().split(", ")
for name in usernames:
    if verification_succesful(name):
        print(name)


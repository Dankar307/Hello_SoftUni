username_list = input().split(", ")
def valid_lenght(username):
    if 3 <= len(username) <= 16:
        return True

    return False


def valid_symbols(username):
    if not (username.isalnum() or "-" in username or "_" in username):
        return False
    return True

def no_redundant_symbol(username):
    if " " in username:
        return False
    return True

def is_valid(name):
    if valid_lenght(name) and valid_symbols(name) and no_redundant_symbol(name):
        return True
    return False


for names in username_list:
    if is_valid(names):
        print(names)
def pass_is_valid(password):
    not_valid_list = []

    if len(password) < 6 or len(password) > 10:
        not_valid_list.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        not_valid_list.append("Password must consist only of letters and digits")
    digit_counter = 0
    for sign in password:
        if sign.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        not_valid_list.append("Password must have at least 2 digits")
    return not_valid_list

given_password = input()
current_validation = pass_is_valid(given_password)
if len(current_validation) == 0:
    print("Password is valid")
else:
    print("\n".join(current_validation))
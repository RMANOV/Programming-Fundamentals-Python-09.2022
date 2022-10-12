
def password_validator_len(password):
    if len(password) < 6 or len(password) > 10:
        return False
    return True


def passord_validator_digit(password):
    if not any(char.isdigit() for char in password):
        return False
    return True

    # if not any(char.isupper() for char in password):
    #     return False
    # if not any(char.islower() for char in password):
    #     return False
def passord_validator_special(password):
    if not any(char.isalnum() for char in password):
        return False
    return True


password = input().strip()

if password_validator_len(password) and passord_validator_digit(password) and passord_validator_special(password):
    print("Password is valid")
else:
    if not password_validator_len(password):
        print("Password must be between 6 and 10 characters")
    if not passord_validator_digit(password):
        print("Password must have at least 2 digits")
    if not passord_validator_special(password):
        print("Password must consist only of letters and digits")
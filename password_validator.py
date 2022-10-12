
def password_validator(password):
        
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters long.")
        # return False

    # if not any(char.isupper() for char in password):
    #     return False
    # if not any(char.islower() for char in password):
    #     return False

    if (char.isalpha() for char in password):
        print("Password must consist only of letters and digits")
        # return False

    if (char.isdigit() for char in password):
        print("Password must have at least 2 digits")
        # return False

    if password_validator(password):
        return True
    else:
        return False



password = input()
if password_validator(password):
    print("Valid password.")
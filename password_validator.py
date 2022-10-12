
def password_validator(password):
    """Validate a password.

    The password must be at least 8 characters long and contain at least
    one uppercase letter, one lowercase letter, and one digit.
    """
    if len(password) < 6 and len(password) > 10:
        print("Password must be between 6 and 10 characters long.")
        return False
        
    # if not any(char.isupper() for char in password):
    #     return False
    # if not any(char.islower() for char in password):
    #     return False

    if (char.isalpha()<2 for char in password):
        print("Password must consist only of letters and digits")
        return False

    if (char.isdigit()<2 for char in password):
        print("Password must have at least 2 digits")
        return False

    return True





password = input("Enter a password: ")
if password_validator(password):
    print("Valid password.")
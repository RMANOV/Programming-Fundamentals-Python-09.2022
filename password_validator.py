
def password_validator(password):
    """Validate a password.

    The password must be at least 8 characters long and contain at least
    one uppercase letter, one lowercase letter, and one digit.
    """
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True


    """Validate a password."""
password = input("Enter a password: ")
if password_validator(password):
    print("Valid password")
else:
    print("Invalid password")

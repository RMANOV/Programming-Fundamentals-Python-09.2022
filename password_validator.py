

def password_validator(password):
    """Checks if password is valid"""
    if 6 > len(password) < 10:
        print("Password must be between 6 and 10 characters")
        # return False
    # if password.islower():
    #     return False
    # if password.isupper():
    #     return False
    if password.isdigit() < 2:
        print("Password must have at least 2 digits")
        # return False
    if password.isalpha():
        print("Password must consist only letters and digits")
        # return False
    else:
        return("Password is valid")
        # return True
    # print("Password is valid")
    # return True





pass_word = input()
print(password_validator(pass_word))

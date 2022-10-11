

def password_validator(password):
    """Checks if password is valid"""
    if 6 < len(password) < 10:
        print("Password must be between 6 and 10 characters")
        # return False
    # if password.islower():
    #     return False
    # if password.isupper():
    #     return False
    elif password.isdigit():
        print("Password must consist only of letters and digits")
        # return False
    elif password.isalpha():
        print("Password must consist only of letters and digits")
        # return False
    else:
        print("Password is valid")
        return True
    # print("Password is valid")
    # return True





pass_word = input()
print(password_validator(pass_word))

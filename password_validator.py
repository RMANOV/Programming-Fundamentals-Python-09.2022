

def password_validator_len(password):
    """Checks if password is valid"""
    if 6 > len(password) < 10:
        print("Password must be between 6 and 10 characters")
        return False
def password_validator_digit(password1):
    if password1.isdigit() < 2:
        print("Password must have at least 2 digits")
        return False
def password_validator_alfa(password2):
    if password2.isalpha():
        print("Password must consist only letters and digits")
        return False

# return("Password is valid")
        # return True
    # print("Password is valid")
    # return True

pass_word = input()
if password_validator_len(pass_word) == False:
    password_validator_len(pass_word)
elif password_validator_digit(pass_word) == False:
    password_validator_digit(pass_word)
elif password_validator_alfa(pass_word) == False:
    password_validator_alfa(pass_word)
else:
    print("Password is valid")

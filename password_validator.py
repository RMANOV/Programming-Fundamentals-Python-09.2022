
def password_validator_len(password):
    if len(password) < 6 or len(password) > 10:
        return("Password must be between 6 and 10 characters")
        # return False


def password_validator_digit(password1):
    if password1.isdigit() < 2:
        return("Password must have at least 2 digits")
        # return False


def password_validator_alfa(password2):
    if password2.isalpha():
        return("Password must consist only letters and digits")
        # return False


pass_word = input()

if password_validator_len(pass_word) is not None:
    print(password_validator_len(pass_word))
if password_validator_digit(pass_word) is not None:
    print(password_validator_digit(pass_word))
elif password_validator_alfa(pass_word) is not None:
    print(password_validator_alfa(pass_word))
else:
    print("Password is valid")

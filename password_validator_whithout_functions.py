password_input = input()
password = password_input.strip()
password_len = len(password)
password_digit = 0
password_special = 0
password_valid = True


for char in password:
    if char.isdigit():
        password_digit += 1
    if not char.isalnum():
        password_special += 1

if password_len < 6 or password_len > 10:
    password_valid = False
    print("Password must be between 6 and 10 characters")

if password_digit < 2:
    password_valid = False
    print("Password must have at least 2 digits")

if password_special > 0:
    password_valid = False
    print("Password must consist only of letters and digits")


if password_valid:
    print("Password is valid")

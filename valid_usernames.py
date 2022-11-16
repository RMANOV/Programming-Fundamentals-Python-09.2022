

initial_list = input().split(", ")
valid_usernames = []

for username in initial_list:
    if 3 < len(username) < 16:
        if username.isalnum() or "-" in username or "_" in username:
            valid_usernames.append(username)

print(*valid_usernames, sep="\n")



users = {}
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    if command[0] == "register":
        username = command[1]
        license_plate_number = command[2]
        if username not in users:
            users[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif command[0] == "unregister":
        username = command[1]
        if username not in users:
            print(f"ERROR: user {username} not found")
        else:
            users.pop(username)
            print(f"{username} unregistered successfully")

print(*[f"{user} => {users[user]}" for user in users], sep="\n" if len(users) == 0 else "\n")
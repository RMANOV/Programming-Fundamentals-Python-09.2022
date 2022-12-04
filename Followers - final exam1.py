

# Input
# •	The possible commands are:
# o	"Log out"
# o	"New follower: {username}"
# o	"Like: {username}: {count}"
# o	"Comment: {username}"
# o	"Blocked: {username}"
# Output
# •	The possible outputs are:
# o	"{Username} doesn't exist."
# o	"{count} followers
# {username}: {likes+comments}
# {username}: {likes+comments}
# …
# {username}: {likes+comments}"

folowers = {}
while True:
    command = input()
    if command == "Log out":
        break
    command = command.split(": ")
    if command[0] == "New follower":
        username = command[1]
        if username not in folowers:
            folowers[username] = [0, 0]
    elif command[0] == "Like":
        username = command[1]
        count = int(command[2])
        if username not in folowers:
            folowers[username] = [count, 0]
        else:
            folowers[username][0] += count
    elif command[0] == "Comment":
        username = command[1]
        if username not in folowers:
            folowers[username] = [0, 1]
        else:
            folowers[username][1] += 1
    elif command[0] == "Blocked":
        username = command[1]
        if username not in folowers:
            print(f"{username} doesn't exist.")
        else:
            del folowers[username]
print(f"{len(folowers)} followers")
for key, value in folowers.items():
    print(f"{key}: {sum(value)}")
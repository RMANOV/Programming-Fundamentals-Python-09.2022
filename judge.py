

# You will receive several input lines in one of the following formats:
# "{username} -> {contest} -> {points}"
# The "contest" and "username" are strings, the given "points" will be an integer number. 
# You need to keep track of every contest and points of each user: 
# •	If the user has already participated in the contest, update their points only if the new ones are more than the older ones.
# •	Otherwise, just save the data - contest, username, and points.
# Also, you need to keep individual statistics for each user - his/her final total points for all contests.
# You should end your program when you receive the command "no more time". 
# At that point, you should print each contest in order of input, for each contest print the participants 
# ordered by points in descending order, then ordered by name in ascending order. 
# After that, you should print individual statistics for every participant ordered by total points in descending order, 
# and then by alphabetical order.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	Username and contest name always will be one word.
# •	Points will be an integer in the range [0, 1000].
# •	There will be no invalid input lines.
# •	If all sorting criteria fail, the order should be by order of input.
# •	The input ends when you receive the command "no more time".
# Output
# •	The output format for the contests is:
# "{constest_name}: {number_participants} participants
# 1. {username1} <::> {points}
# 2. {username2} <::> {points}
# …
# {N}. {usernameN} <::> {points}"
# •	After you print all contests, print the individual statistics for every participant.
# •	The output format is:
# "Individual standings:
# 1.	{username1} -> {total_points}
# 2.	{username} -> {total_points}
# …
# {N}. {username} -> {total_points}"
# Outpu for the example:
# Algo: 3 participants
# 1. Peter <::> 400
# 2. George <::> 300
# 3. Simo <::> 200
# DS: 2 participants
# 1. Mariya <::> 600
# 2. Peter <::> 150
# Individual standings:
# 1. Mariya -> 600
# 2. Peter -> 550
# 3. George -> 300
# 4. Simo -> 200

users = {}

# Read input
command = input()
while command != "no more time":
    username, contest, points = command.split(" -> ")
    points = int(points)
    if contest not in users:
        users[contest] = {}
    if username not in users[contest]:
        users[contest][username] = points
    else:
        if users[contest][username] < points:
            users[contest][username] = points
    command = input()

# # Print results
# for contest, data in users.items():
#     print(f"{contest}: {len(data)} participants")
#     # print(*[f"{i + 1}. {name} <::> {points}" for i, (name, points) in enumerate(sorted(data.items(), key=lambda x: (-x[1], x[0])))], sep=" " * 2)
#     for i, (name, points) in enumerate(sorted(data.items(), key=lambda x: (-x[1], x[0]))):
#         print(f"{i + 1}. {name} <::> {points}")

# print("Individual standings:")
# # print(*[f"{i + 1}. {k} -> {v}" for i, (k, v) in enumerate(sorted(users.items(), key=lambda x: x[1], reverse=True))], sep="")
# for i, (k, v) in enumerate(sorted(users.items(), key=lambda x: x[1], reverse=True)):
#     print(f"{i + 1}. {k} -> {v}")

# # Print results - 2nd way - do not use enumerate
for contest, data in users.items():
    print(f"{contest}: {len(data)} participants")
    # print(*[f"{i + 1}. {name} <::> {points}" for i, (name, points) in enumerate(sorted(data.items(), key=lambda x: (-x[1], x[0])))], sep=" " * 2)
    for i, (name, points) in enumerate(sorted(data.items(), key=lambda x: (-x[1], x[0]))):
        print(f"{i + 1}. {name} <::> {points}")

print("Individual standings:")
# print(*[f"{i + 1}. {k} -> {v}" for i, (k, v) in enumerate(sorted(users.items(), key=lambda x: x[1], reverse=True))], sep="")
# first - sort by values, then by keys, then reverse the list, then print it
############################################################################################################
# Traceback (most recent call last):
#   File "/tmp/ExecutionStrategies/lfebkzj2.z0i/tmpKV02RP.tmp", line 39, in <module>
#     users = dict(sorted(users.items(), key=lambda x: (x[1], x[0]), reverse=True))
# TypeError: '<' not supported between instances of 'dict' and 'dict'
############################################################################################################
# users = dict(sorted(users.items(), key=lambda x: (x[1], x[0]), reverse=True))
while users:
    counter = 1
    user, points = users.popitem()
    print(f"{counter}. {user} -> {points}")
    counter += 1
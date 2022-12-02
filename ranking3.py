# You will receive some lines of input in the format "{contest}:{password for contest}" until you receive "end of contests".
# Save that data because you will need it later.
# After that, you will receive another type of inputs in the format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions". Here is what you need to do.
# •	Check if the contest is valid (It is considered valid if you received it in the first type of input)
# •	Check if the password is correct for the given contest
# •	If the contest and the password are valid,
# save the user with the contest they take part in (a user can take part in many contests) and the points the user has in the given contest.
# If you receive the same contest and the same user, update the points only if the new ones are more than the older ones.
# In the end, you should print the info for the user with the most points (total points for all contents they participated in) in the format "Best candidate is {user} with total {total_points} points.".
# After that print all students ordered by their names.
# For each user print each contest with the points in descending order.
# Input
# •	Strings in format "{contest}:{password for contest}" until the "end of contests" command. There will be no case with two equal contests
# •	Strings in format "{contest}=>{password}=>{username}=>{points}" until the "end of submissions" command.
# •	There will be no case with 2 or more users with the same total points!
# Output
# •	On the first line, print the best user in the format "Best candidate is {user} with total {total points} points.".
# •	Then print all students ordered as mentioned above in the format:
# "{user_name1}
# #  {contest1} -> {points}
# #  {contest2} -> {points}
# …
# #  {contestN} -> {points}"
# Constraints
# •	The strings may contain any ASCII character except (:, =, >).
# •	The numbers will be in the range [0 - 10000].
# •	Second input is always valid.

# Fill the dictionary without missing literals
# contests_passwords = {contest : password for contest, password in [input().split(":") for _ in range(int(input()))] if input() != "end of contests"}
contests_passwords = {contest : password for contest, password in [input().split(":") for _ in range(100)] if input() != "end of contests"}
user_contests_points = {user : {contest : int(points) for contest, password, user, points in [input().split("=>") for _ in range(int(input()))] if contest in contests_passwords and password == contests_passwords[contest]} for user in [input().split("=>")[2] for _ in range(int(input()))] if input() != "end of submissions"}

# calculate total points for each user and find the best user
best_user = max(user_contests_points, key=lambda user: sum(user_contests_points[user].values()))

# print the best user
print(f"Best candidate is {best_user} with total {sum(user_contests_points[best_user].values())} points.")

# print all users
print("\n".join([f"{user}\n#  {'' if len(user_contests_points[user]) == 0 else ''}\n#  ".join([f"{contest} -> {points}" for contest, points in sorted(user_contests_points[user].items(), key=lambda contest_points: -contest_points[1])]) for user in sorted(user_contests_points)]))


# users = {name :[contest,points]

# command1 = input()
# while command1 != "end of contests":
#     contest, password = command1.split(":")
#     users[contest] = password
#     command1 = input()

# command2 = input()
# while command2 != "end of submissions":
#     contest, password, username, points = command2.split("=>")
#     if contest in users and password == users[contest]:
#         if username not in users:
#             users[username] = {}
#         if contest not in users[username]:
#             users[username][contest] = int(points)
#         else:
#             if int(points) > users[username][contest]:
#                 users[username][contest] = int(points)
#     command2 = input()

# # calculate maximum points and the best user
# best_user = ""
# max_points = 0

# for user, contests in users.items():
#     user_points = 0


# # for user in users:
# #     current_points = 0
# #     for contest in users[user]:
# #         current_points += int(users[user][points])
# #     if current_points > total_points:
# #         total_points = current_points
# #         best_user = user

# # print the best user

# print(f"Best candidate is {best_user} with total {total_points} points.")
# for user in sorted(users):
#     if user != best_user:
#         print(f"{user}")
#         for contest in sorted(users[user], key=lambda x: -users[user][x]):
#             print(f"#  {contest} -> {users[user][contest]}")










# contests = {}
# users = {}


# def aquire_input():
#     command = input()
#     while command != "end of contests":
#         command = input()
#         if command != "end of contests":
#             contest, password = command.split(":")
#             contests[contest] = password


# def aquire_submissions():
#     command = input()
#     while command != "end of submissions":
#         command = input()
#         if command != "end of submissions":
#             contest, password, user, points = command.split("=>")
#             if contest in contests:
#                 if contests[contest] == password:
#                     if user not in users:
#                         users[user] = {}
#                         users[user][contest] = int(points)
#                     else:
#                         if contest not in users[user]:
#                             users[user][contest] = int(points)
#                         else:
#                             if users[user][contest] < int(points):
#                                 users[user][contest] = int(points)


# def print_result():
#     best_user = ""
#     best_points = 0
#     for user in users:
#         total_points = 0
#         for contest in users[user]:
#             total_points += users[user][contest]
#         if total_points > best_points:
#             best_points = total_points
#             best_user = user
#     print(f"Best candidate is {best_user} with total {best_points} points.")
#     print("Ranking:")
#     for user in sorted(users):
#         print(user)
#         for contest in sorted(users[user], key=users[user].get, reverse=True):
#             print(f"#  {contest} -> {users[user][contest]}")


# def main():
#     aquire_input()
#     aquire_submissions()
#     print_result()


# main()

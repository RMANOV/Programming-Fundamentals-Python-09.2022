

# You will receive several input lines in one of the following formats:
# "{player} -> {position} -> {skill}"
# "{player} vs {player}"
# The "player" and "position" are strings, and the given "skill" will be an integer number. 
# You need to keep track of every player.
# When you receive a player with his position and skill, add him to the players' pool, if he isn`t present, 
# else add his position and skill or update his skill, only if the current position skill is lower than the new value.
# If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
# •	If they got at least one position in common, the player with better total skill points wins and the other is demoted from the tier -> remove him. 
# •	If they have the same total skill points at the same positions, the duel is a tie and they both continue in the Season.
# •	If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
# You should end your program when you receive the command "Season end". 
# At that point, you should print the players, ordered by total skill in descending order, then ordered by player name in ascending order. 
# For each player print their position and skill ordered descending by skill, then ordered by position name in ascending order.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	Player and position will always be one-word strings, containing no whitespaces.
# •	Skill will be an integer in the range [0, 1000].
# •	There will be no invalid input lines.
# •	The program ends when you receive the command "Season end".
# Output
# •	The output format for each player is:
# "{player}: {total_skills} skill"
# - {position1} <::> {skill}
# - {position2} <::> {skill}
# …
# - {positionN} <::> {skill}"

# Input:
# Pesho -> BattleCry -> 400
players = {}
command = input()
while command != "Season end":
    if " -> " in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in players:
            players[player] = {position: skill}
        else:
            if position not in players[player]:
                players[player][position] = skill
            else:
                if players[player][position] < skill:
                    players[player][position] = skill
    else:
        player1, player2 = command.split(" vs ")
        if player1 in players and player2 in players:
            for position in players[player1]:
                if position in players[player2]:
                    if players[player1][position] > players[player2][position]:
                        del players[player2]
                        break
                    elif players[player1][position] < players[player2][position]:
                        del players[player1]
                        break
    command = input()

# sort the players by total skill in descending order, then by name in ascending order
sorted_players = sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0]))

# print the result
# print("Players in the league:")
print(*[f"{player}: {sum(skills.values())} skill\n" + "\n".join([f"- {position} <::> {skill}" for position, skill in sorted(skills.items(), key=lambda x: (-x[1], x[0]))]) for player, skills in sorted_players], sep="\n")

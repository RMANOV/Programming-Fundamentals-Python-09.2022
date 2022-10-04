

team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
players=input().split()
removed_players = []

game_was_terminted = False

for i in range(len(players)):    
    if players[i] in removed_players:
        continue
    else:
        removed_players.append(players[i])
        
    if players[i] in team_a:
        team_a.remove(players[i])
    else:
        team_b.remove(players[i])
    if len(team_a) < 7 or len(team_b) < 7:
        
        game_was_terminted = True
        break

if not game_was_terminted:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")    
else:
        print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
        print(f"Game was terminated")

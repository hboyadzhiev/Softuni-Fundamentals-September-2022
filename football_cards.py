cards = input().split()
sent_off_players = []
team_a = 11
team_b = 11
terminated = False

for player in cards:
    if player in sent_off_players:
        continue
    else:
        sent_off_players.append(player)
        if player[0] == "A":
            team_a -= 1
        elif player[0] == "B":
            team_b -= 1
    if team_a < 7 or team_b < 7:
        terminated = True
        break
print(f"Team A - {team_a}; Team B - {team_b}")
if terminated:
    print("Game was terminated")



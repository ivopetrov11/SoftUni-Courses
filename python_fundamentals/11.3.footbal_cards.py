team_a = [f"A-{number}" for number in range(1,12)]
# print(team_a)
team_b = [f"B-{number}" for number in range(1,12)]
# print(team_b)

players_cards = input()
players_cards_list = players_cards.split(" ")
terminated_game = False

for card in players_cards_list:
    if card in team_a:
        team_a.remove(card)
    elif card in team_b:
        team_b.remove(card)

    if len(team_a) < 7 or len(team_b) < 7:
        terminated_game = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if terminated_game:
    print("Game was terminated")
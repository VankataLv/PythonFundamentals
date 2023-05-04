user_input = input()
team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# --variant--
# team_a = ["A-" + str(s) for s in range(1, 12)]
# same for team_b "B"
red_cards_log = user_input.split(" ")
team_punished = ""
player_punished = ""
special_7 = False
for red_card in red_cards_log:
    if red_card[0] == "A":
        if len(red_card) == 4:
            player_punished = red_card[2:4]
        else:
            player_punished = red_card[2]
        if int(player_punished) in team_A:
            team_A.remove(int(player_punished))
        if len(team_A) < 7:
            special_7 = True
            break

    elif red_card[0] == "B":
        if len(red_card) == 4:
            player_punished = red_card[2:4]
        else:
            player_punished = red_card[2]
        if int(player_punished) in team_B:
            team_B.remove(int(player_punished))
        if len(team_B) < 7:
            special_7 = True
            break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if special_7:
    print("Game was terminated")

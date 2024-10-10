string_of_cards = input()
list_of_cards = string_of_cards.split()
team_a_players_cards = []
team_b_players_cards = []
team_a_players = 11
team_b_players = 11
for player_card in list_of_cards:
    if team_a_players > 7 and team_b_players > 7:

        if 'A' in player_card:
            if player_card in team_a_players_cards:
                continue
            else:
                team_a_players_cards.append(player_card)
                team_a_players -= 1


        else:

            if player_card in team_b_players_cards:
                continue
            else:
                team_b_players_cards.append(player_card)
                team_b_players -= 1
    else:
        if team_a_players > team_b_players:
            team_b_players -= 1
        else:
            team_a_players -= 1
        print(f"Team A - {team_a_players}; Team B - {team_b_players}")
        print("Game was terminated")
        exit()


print(f"Team A - {team_a_players}; Team B - {team_b_players}")
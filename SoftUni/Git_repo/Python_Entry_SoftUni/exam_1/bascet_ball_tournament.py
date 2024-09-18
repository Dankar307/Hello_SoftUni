match_win_count = 0
match_lose_count = 0
num_of_rounds = 0
round_ma = 0
while True:
    name = input()
    if name != 'End of tournaments':

        num_of_rounds = int(input())
        for round in range(1, num_of_rounds + 1):
            round_ma += 1
            desis_team_points = int(input())
            enemy_points = int(input())
            if desis_team_points > enemy_points:
                match_win_count += 1
                print(f"Game {round} of tournament {name}: win with {abs(desis_team_points - enemy_points)} points.")
            else:
                match_lose_count += 1
                print(f"Game {round} of tournament {name}: lost with {abs(desis_team_points - enemy_points)} points.")
    else:
        break
win_percentage = (match_win_count / round_ma) * 100
lost_percentage = (match_lose_count / round_ma) * 100
print(f'{win_percentage:.2f}% matches win')
print(f'{lost_percentage:.2f}% matches lost')


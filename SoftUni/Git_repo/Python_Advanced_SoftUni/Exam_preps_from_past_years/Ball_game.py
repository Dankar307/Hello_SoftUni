from collections import deque


strength = [int(x) for x in input().split()]
accuracy = deque(int(x) for x in input().split())
total_goals = 0
while accuracy and strength:
    sum_of_player = strength[-1] + accuracy[0]
    if sum_of_player == 100:
        total_goals += 1
        strength.pop()
        accuracy.popleft()
    elif sum_of_player < 100:
        if strength[-1] < accuracy[0]:
            strength.pop()
        elif strength[-1] > accuracy[0]:
            accuracy.popleft()
        else:
            strength[-1] += accuracy[0]

            accuracy.popleft()

    else:
        strength[-1] -= 10
        accuracy.rotate(-1)
if not total_goals:
    print("Paul failed to score a single goal.")
elif 0 < total_goals < 3:
    print(f"Paul failed to make a hat-trick.\nGoals scored: {total_goals}")
elif total_goals == 3:
    print(f"Paul scored a hat-trick!\nGoals scored: {total_goals}")
else:
    print(f"Paul performed remarkably well!\nGoals scored: {total_goals}")
if strength:
    print(f"Strength values left: {', '.join(str(i) for i in strength)}", )
if accuracy:
    print(f"Accuracy values left: {', '.join(str(i) for i in accuracy)}")

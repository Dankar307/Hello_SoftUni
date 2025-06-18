from collections import deque


full_string = deque(input().split())
main_colors = ["red","blue","yellow"]
secondary_colors = {"green":["yellow", "blue"],"purple":["red", "blue"],"orange":["red", "yellow"]}
found_colors = []
while full_string:
    first_string = full_string.popleft()
    last_string = full_string.pop() if full_string else ""
    for color in (first_string + last_string, last_string + first_string):
        if color in main_colors or color in secondary_colors:
            found_colors.append(color)
            break

    else:
        middle = len(full_string) // 2
        if len(first_string) > 1:
            full_string.insert(middle,first_string[:-1])
        if len(last_string) > 1:
            full_string.insert(middle,last_string[:-1])
for color in found_colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in found_colors:
                found_colors.remove(color)
                break
print(found_colors)
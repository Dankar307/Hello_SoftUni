from collections import deque
number_of_pumps = int(input())
pumps = deque()

for _ in range(number_of_pumps):
    fuel, distance = input().split()
    pumps.append({"fuel": int(fuel), "distance": int(distance)})

starting_destination = 0
stops = 0

while stops < number_of_pumps:
    fuel = 0
    distance = 0
    for i in range(number_of_pumps):
        fuel += pumps[i]["fuel"]
        distance += pumps[i]["distance"]
        if fuel < distance:
            starting_destination += 1
            stops = 0
            pumps.rotate(-1)
            break
        else:
            stops += 1
print(starting_destination)
from collections import deque
from sys import maxsize

food_quantity = int(input())

queue = deque(int(x) for x in input().split(" "))
print(max(queue))


while queue and queue[0] <= food_quantity:
    food_quantity -= queue.popleft()
if queue:
    print(f"Orders left:", *queue)
else:
    print("Orders complete")
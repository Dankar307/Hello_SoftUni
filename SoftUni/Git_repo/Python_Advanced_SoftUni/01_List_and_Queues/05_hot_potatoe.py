from collections import deque
queue = deque(x for x in input().split())
n = int(input())
while queue:
    if len(queue) == 1:
        break
    queue.rotate(-(n-1))
    removed_kid = queue.popleft()
    print(f"Removed {removed_kid}")

removed_kid = queue.popleft()
print(f"Last is {removed_kid}")
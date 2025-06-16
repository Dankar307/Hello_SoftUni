N = int(input())
guest_list = set()

for _ in range(N):
    guest_list.add(input())

command = input()
while command != "END":
    guest_list.remove(command)
    command = input()

print(f"{len(guest_list)}\n" + "\n".join(sorted(guest_list)))
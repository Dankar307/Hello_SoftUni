N = int(input())
parking_lot = set()

for _ in range(N):
    keyword, command = input().split(", ")
    if keyword == "IN":
        parking_lot.add(command)
    elif keyword == "OUT":
        parking_lot.remove(command)
    else:
        pass # In case of wrong command
if parking_lot:
    print("\n".join(parking_lot))
else:
    print("Parking Lot is Empty")
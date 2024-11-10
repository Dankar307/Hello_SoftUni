N = int(input())
parking_lot = {}
for cars in range(N):
    command = input()

    if "unregister" in command:
        unreg_, name = command.split()
        if name not in parking_lot.keys():

                print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            parking_lot.pop(name)
    elif "register" in command:
        reg_, name, license_plate = command.split()
        if name in parking_lot.keys():
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            print(f"{name} registered {license_plate} successfully")
            parking_lot[name] = license_plate
for name, license_plate in parking_lot.items():
    print(f"{name} => {license_plate}")
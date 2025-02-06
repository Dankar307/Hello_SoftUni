n = int(input())
mileage = 0
car_collection = {}
for cars in range(n):
    car,mileage,fuel = input().split("|")
    car_collection[car] = {"mileage":int(mileage),"fuel":int(fuel)}

while True:
    commands = input().split(" : ")

    if commands[0] == "Stop":
        break
    if commands[0] == "Drive":
        car, distance, fuel = commands[1], int(commands[2]), int(commands[3])
        if car_collection[f"{car}"]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            car_collection[f"{car}"]["fuel"] -= fuel
            car_collection[f"{car}"]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if car_collection[f"{car}"]["mileage"] >= 100000:
            car_collection.pop(car)
            print(f"Time to sell the {car}!")

    elif commands[0] == "Refuel":
        car, fuel = commands[1], int(commands[2])
        if car_collection[f"{car}"]["fuel"] + fuel > 75:
            difference = 75 - car_collection[f"{car}"]["fuel"]
            print(f"{car} refueled with {difference} liters")
            car_collection[f"{car}"]["fuel"] = 75
        else:
            car_collection[f"{car}"]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif commands[0] == "Revert":
        car,mileage = commands[1],int(commands[2])

        car_collection[f"{car}"]["mileage"] -= mileage
        print(f"{car} mileage decreased by {mileage} kilometers")
        if car_collection[f"{car}"]["mileage"] < 10000:
            car_collection[f"{car}"]["mileage"] = 10000
for car,pack in car_collection.items():
    mileage,fuel = pack.values()
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
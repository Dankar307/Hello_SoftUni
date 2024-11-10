countries = input().split(", ")
capitals = input().split(", ")

info = dict(zip(countries,capitals))
for key, value in info.items():
    print(f"{key} -> {value}")
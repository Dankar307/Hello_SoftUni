hour = int(input())
day_of_week = input()

if 10 <= hour <= 18:

    if not (day_of_week == "Sunday"):
        print("open")
    else:
        print("closed")

else:
    print("closed")



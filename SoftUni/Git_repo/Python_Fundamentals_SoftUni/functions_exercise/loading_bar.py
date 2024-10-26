def loading_bar(percent:int):
    if 0 < percent < 100:
        print(f"{percent}% [", end = "")
        for i in range(0, percent//10):
            print("%", end="")
        for j in range(0, 10 - (percent // 10)):
            print(".",end="")
        print("]\nStill loading...")

    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")


percent = int(input())
loading_bar(percent)
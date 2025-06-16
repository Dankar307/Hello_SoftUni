from collections import deque
besinput = "20 62 99 35 0 150"
nctarinput = "120 60 10 1 70 10"
symbolinput = "+ - + + / * - - /"
bees = deque(int(x) for x in besinput.split())
nectar = [int(x) for x in nctarinput.split()]
symbols = deque(symbolinput.split())

honey = 0

operators = {
  "+": lambda x,y: x+y,
  "-": lambda x,y: x-y,
  "*": lambda x,y: x*y,
  "/": lambda x,y: x/y if y > 0 else 0 # In case of a wrong answer check here
}

while bees and nectar:
    if bees[0] >= nectar[-1]:
        honey += abs(operators[symbols[0]](bees[0], nectar[-1]))
        bees.popleft()
        nectar.pop()
        symbols.popleft()
    else:
        nectar.pop()


print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {", ".join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {", ".join(str(x) for x in nectar)}")
a = int(input())
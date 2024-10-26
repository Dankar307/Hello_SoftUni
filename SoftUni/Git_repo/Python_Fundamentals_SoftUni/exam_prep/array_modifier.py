array = [int(num) for num in input().split()]
def swap(index1: int, index2: int):

    array[index1], array[index2] = array[index2], array[index1]
    return array





command = input()
while "end" not in command:
    if "swap" in command:
        swaps, index1, index2 = command.split()
        index1 = int(index1)
        index2 = int(index2)
        swap(index1, index2)

    elif "multiply" in command:
        multiply, i1, i2 = command.split()
        i1 = int(i1)
        i2 = int(i2)
        array[i1] = array[i1] * array[i2]
    else:
        for i in array:
            i -= 1
for i in array:
    print( f"{i}, ")
n = int(input())
piece_collection = {}
for piece in range(n):
    painting,composer,key = input().split("|")
    piece_collection[painting] = {"composer":composer,"key":key}
while True:
    command = input().split("|")
    if command[0] == "Stop":
        break

    if command[0] == "Add":

        piece,composer,key = command[1],command[2],command[3]

        if piece not in piece_collection.keys():
            piece_collection[piece] = {"composer":composer,"key":key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command[0] == "Remove":
        piece = command[1]
        if piece in piece_collection.keys():
            piece_collection.pop(f"{piece}")
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command[0] == "ChangeKey":
        piece,key = command[1],command[2]
        if piece in piece_collection.keys():
            piece_collection[f"{piece}"]["key"] = key
            print(f"Changed the key of {piece} to {key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece,parts in piece_collection.items():
    composer = parts["composer"]
    key = parts["key"]
    print(f"{piece} -> Composer: {composer}, Key: {key}")
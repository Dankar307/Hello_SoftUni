while True:

    string = input()

    if string == "end":
        break
    word = string
    string = string[::-1]
    print(f"{word} = {string}")

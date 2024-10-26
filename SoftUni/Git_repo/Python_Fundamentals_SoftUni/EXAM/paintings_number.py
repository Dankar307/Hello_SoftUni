list_of_paintings = [int(num) for num in input().split()]
while True:
    command = input()
    if "END" not in command:
        if "Change" in command:
            change, painting_number , new_number = command.split()
            painting_number = int(painting_number)
            new_number = int(new_number)
            if painting_number in list_of_paintings:
                index = list_of_paintings.index(painting_number)
                list_of_paintings[index] = new_number
        elif "Hide" in command:
            hide, painting_number = command.split()
            painting_number = int(painting_number)
            if painting_number in list_of_paintings:
                list_of_paintings.remove(painting_number)
        elif "Switch" in command:
            switch, painting_num_1, painting_num_2 = command.split()
            painting_num_1 = int(painting_num_1)
            painting_num_2 = int(painting_num_2)
            if painting_num_1 in list_of_paintings and painting_num_2 in list_of_paintings:
                index_1 = list_of_paintings.index(painting_num_1)
                index_2 = list_of_paintings.index(painting_num_2)
                list_of_paintings[index_1], list_of_paintings[index_2] = list_of_paintings[index_2], list_of_paintings[index_1]
        elif "Insert" in command:
            insert,index,painting_number = command.split()
            index = int(index)
            painting_number = int(painting_number)
            if index in range(0, len(list_of_paintings) +1):
                list_of_paintings.insert(index + 1, painting_number)
        elif "Reverse" in command:
            list_of_paintings.reverse()

    else:
        for i in list_of_paintings:
            print(i, end=" ")

        break
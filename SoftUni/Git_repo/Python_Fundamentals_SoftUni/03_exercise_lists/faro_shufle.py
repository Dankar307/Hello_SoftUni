cards_as_string = input().split()
number_of_cards = int(input())
midle_of_deck = len(cards_as_string) // 2
shufled_deck = []
new_deck = cards_as_string
for i in range(1, number_of_cards + 1):
    left_part = new_deck[:midle_of_deck]
    right_part = new_deck[midle_of_deck:]
    for cards in range(0, len(cards_as_string)//2):

        shufled_deck.append(left_part[cards])
        shufled_deck.append(right_part[cards])
    new_deck = shufled_deck
    shufled_deck = []

print(new_deck)



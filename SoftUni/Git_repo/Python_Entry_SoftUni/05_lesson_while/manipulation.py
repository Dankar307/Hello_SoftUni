import random
fruits = ['🍇','🍈','🍉','🍊','🍋','🍌']

balance = int(input("ENTER YOUR BAALANCE: "))

while balance > 0:
    print(f'Your current balance is: {balance}')
    bet = int(input("Place your bet: "))
    while bet > balance:
        print("Insufficient balance!")
        bet = int(input('place your bet: '))
    reel1 = random.choice(fruits)
    reel2 = random.choice(fruits)
    reel3 = random.choice(fruits)

    if reel1 == reel2 or reel2 == reel3:
        





else:
    print("You have no money left!")


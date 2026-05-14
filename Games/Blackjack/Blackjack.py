import randomyyy

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def check_blackjack(card1 , card2):
    if (card1 == [10,11] or [11,10]) and (card2 == [10,11] or [11,10]) :
        print("Both the user and computer have blackjack.\nIt's a DRAW.")
    elif card1 == [10,11] or [11,10]:
        print("The user has blackjack.\nYOU WON")
    elif card2 == [10,11] or [11,10]:
        print("The computer has blackjack.\nYOU LOST")


def blackjack():
    print("\n" * 20)
    i = 1
    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    print(f"Your cards: {user_cards}, Current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if i==1 :
        check_blackjack(user_cards , computer_cards)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if start == 'y':
    blackjack()


print()
another_card = input("Type 'y' to get another card, type 'n' to pass : ").lower()
if another_card == 'y':
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

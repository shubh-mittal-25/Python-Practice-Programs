import random

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

def deal_card():
    """Return a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score (cards):
    """Calculate the total score of the given cards."""
    total = sum(cards)
    if total == 21 and len(cards) == 2:
        return 0
    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
    return total

def compare(u_score, c_score):
    """Compare user score and computer score."""
    if u_score == c_score:
        return "\nDraw\n".upper()
    elif c_score == 0:
        return "\nLose, computer has Blackjack\n".upper()
    elif u_score == 0:
        return "\nWin with a Blackjack\n".upper()
    elif u_score > 21:
        return "\nYou went over. You lose.\n".upper()
    elif c_score > 21:
        return "\nComputer went over. You win.\n".upper()
    elif u_score > c_score:
        return "\nYou win\n".upper()
    else:
        return "\nYou lose\n".upper()

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass : ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    if user_score == 0:
        print(f"Your final hand: {user_cards}, final score: 21")
    else:
        print(f"Your final hand: {user_cards}, final score: {user_score}")
    if computer_score == 0:
        print(f"Computer's final hand: {computer_cards}, final score: 21")
    else:
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n'") == "y":
    print("\n"*20)
    play_game()
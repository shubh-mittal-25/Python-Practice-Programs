import random
logo = r"""
  ________                                   __  .__                                   ___.                  
 /  _____/ __ __   ____   ______ ______    _/  |_|  |__   ____       ____  __ __  _____\_ |__   ___________  
/   \  ___|  |  \_/ __ \ /  ___//  ___/    \   __\  |  \_/ __ \     /    \|  |  \/     \| __ \_/ __ \_  __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \      |  | |   Y  \  ___/    |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/ 
 \______  /____/  \___  >____  >____  >     |__| |___|  /\___  >   |___|  /____/|__|_|  /___  /\___  >__|    
        \/            \/     \/     \/                \/     \/         \/            \/    \/     \/       
"""

def check_the_number(guess):
    """Check if guess is correct, lower or higher."""
    global number, is_correct
    if guess == number:
        is_correct = True
    elif guess > number:
        print("Too High\nGuess again")
    else :
        print("Too Low\nGuess again")

print(logo)
print("Welcome to Number Guessing Game")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty level: 'easy' or 'hard': ").lower()
attempts = -1
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

number = random.randint(1, 100)
is_correct = False

while attempts > 0 and not is_correct:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess_num = int(input("Make a guess: "))
    check_the_number(guess_num)
    attempts = attempts - 1

if is_correct:
    print(f"Congratulations! You got it.\nThe number was {number}.")
if attempts <=0:
    print(f"Sorry, you have reached the maximum number of attempts.\nYOU LOSE")
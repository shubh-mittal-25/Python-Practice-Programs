import random
from Hangman_words import word_list
from Hangman_art import stages, logo

print(logo)
chosen_word = random.choice (word_list)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

correct_letters = []
lives = 9
game_over = False
while not game_over:
    print(f"****************************{lives}/9 LIVES LEFT****************************")
    guess = input("Guess a letter : ").lower()
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("YOU WIN")


    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"YOU LOSE\nTHE WORD WAS {chosen_word}")

    print(stages[lives])
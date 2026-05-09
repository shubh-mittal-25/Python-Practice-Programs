import random
rock = '''
    ______
---'   ___)
      (______)
      (______)
      (_____)
---.__(____)
'''

paper = '''
    _______
---'   ____)_______
          __________)
          ___________)
         ___________)
---.______________)
'''

scissors = '''
    _______
---'   ____)________
          __________)
       ______________)
      (____)
---.__(___)
'''
options = [rock,paper,scissors]
user_choice = int(input("What do you Choose?\nType 0 for Rock , 1 for Paper or 2 for Scissors\n"))
computer_choice = random.randint(0,2)

if user_choice >=0 and user_choice <=2:
    print(options[user_choice])
    print("Computer Chose :\n" + options[computer_choice])
    if user_choice == computer_choice:
        print("It's a Draw!")
    elif user_choice == 0 and computer_choice == 1:
        print("YOU LOSE!")
    elif user_choice == 0 and computer_choice == 2:
        print("YOU WIN!")
    elif user_choice == 1 and computer_choice == 0:
        print("YOU WIN!")
    elif user_choice == 1 and computer_choice == 2:
        print("YOU LOSE!")
    elif user_choice == 2 and computer_choice == 0:
        print("YOU LOSE!")
    elif user_choice == 2 and computer_choice == 1:
        print("YOU WIN!")

else :
    print("You typed an invalid number, YOU LOSE!")
import random
import art
import game_data

def display(a,b):
    print(f"Compare A : {a['name']}, a {a['description']}, from {a['country']}")
    print(art.vs)
    print(f"Against B : {b['name']}, a {b['description']}, from {b['country']}")

def compare(followers_1, followers_2):
    global score
    choice = input("Who has more instagram followers? Type 'A' or 'B'. : ").lower()
    if choice == 'a':
        if followers_1 >= followers_2:
            score += 1
            return False
        else:
            return True
    elif choice == 'b':
        if followers_1 <= followers_2:
            score +=1
            return False
        else:
            return True
    return False

print(art.logo)
item_A = random.choice(game_data.data)
item_B = random.choice(game_data.data)
score = 0
is_wrong = False

while not is_wrong:
    if score !=0:
        print(f"You're right. Score: {score}")
    display(item_A,item_B)
    is_wrong = compare(item_A['follower_count'],item_B['follower_count'])
    item_A = item_B
    item_B = random.choice(game_data.data)
    print("\n" *30)

print(f"Sorry, that's wrong. Final Score : {score}")


# A = take random dict and print it
# B = take random dict and print it
# ask question
# if correct, A=B and B - take random. Print. Ask question again. score +1
# if wrong, terminate. display final score
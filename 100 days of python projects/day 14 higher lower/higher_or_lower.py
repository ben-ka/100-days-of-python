from game_data import data
import art
import random
import os

def choose_celebrity():
    celeb = random.choice(data)
    return celeb
    
def compare(celebA, celebB):
    if celebA['follower_count'] > celebB['follower_count']:
        return "a"
    elif celebA['follower_count'] < celebB['follower_count']:
        return "b"
    else:
        return "draw"

def user_guess(celebA,celebB):
    print(f"compare: {celebA['name']}, {celebA['description']} from {celebA['country']}")
    print(art.vs)
    print(f"{celebB['name']}, {celebB['description']} from {celebB['country']}")
    more_followers = input("Who has more followers? Type 'A' or 'B': ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    return more_followers

    # main function
def game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print (art.logo)
    score = 0
    while True:
        if score !=0:
            print("you're right!",end=" ")
        print(f"current score: {score}")
        if score == 0:
            celebA = choose_celebrity()            
        celebB = choose_celebrity()
        winner = compare(celebA,celebB)
        guess = user_guess(celebA,celebB)     
        if guess == winner or winner == "draw":
            score+=1
            celebA = celebB
        else:
            print(f"sorry, thats wrong. final score: {score}")
            break
    play_again = input("do you want to play again? type 'yes' or 'no': ")
    if play_again.startswith("y"):
        game()

game()
    
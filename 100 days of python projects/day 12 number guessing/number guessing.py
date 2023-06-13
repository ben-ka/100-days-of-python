import random
import art
print(art.logo)
print("Welcome to the Number Guessing Game!")

def game():
    
    print("I'm thinking of a number between 1 and 100.")
    while True:
        difficulty = input("Choose a difficulty. Easy or Hard: ").lower()
        if difficulty == "easy":
            lives = 10
            
            break
        elif difficulty =="hard" :
            lives = 5
            
            break
        else:
            print("not a valid difficulty")
    number_selected =  number_generator()
                                        
    guess(lives,number_selected)


def number_generator():
    number_selected = random.randint(1,100)
    return number_selected

def guess(lives,number):
    guess = -999
    while guess != number and lives != 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("make a guess: "))
        lives -= 1
        if guess > number:
            print("too high")
            print("guess again")
        elif guess < number:
            print("too low")
            print("guess again")
    if guess == number:
        print(f"you got it, the number is {number}")
    else:
        print(f"you've run out of guesses, the number was {number}")


game()
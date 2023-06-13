import random
import os
import art
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def current_score(current_cards):
    return sum(current_cards)



def draw_random_cards(my_cards,number_of_cards,sum):
    for i in range(number_of_cards):
        card_choice = random.choice(CARDS)
        if card_choice == 11:
            if sum + 11 >21:
                card_choice = 1
        my_cards.append(card_choice)
    return my_cards


def draw_cards_dealer(dealer_cards,dealer_sum):
    while dealer_sum < 17:
        dealer_cards = draw_random_cards(dealer_cards,1,dealer_sum)
        dealer_sum = current_score(dealer_cards)
    return dealer_cards


print(art.logo)    
def main():
   
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play.startswith("y"):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        sum_my_cards =0
        dealer_sum =0
        my_cards = []
        dealer_cards = []
        my_cards = draw_random_cards(my_cards,2,sum_my_cards)
        dealer_cards = draw_random_cards(dealer_cards,1 , dealer_sum)
        dealer_sum = current_score(dealer_cards)
        sum_my_cards = current_score(my_cards)
        print(f"your cards: {my_cards}, current score: {sum_my_cards}")
        print(f"computer's first card: {dealer_cards[0]} ")
        while sum_my_cards <= 21:                           # the loop runs as long as the user's card total is smaller than 21
            do_you_want_to_hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if do_you_want_to_hit.startswith("y"):                                   # deals with person choosing to get another card calls the function to draw a random card each time
                my_cards = draw_random_cards(my_cards,1,sum_my_cards)
                sum_my_cards = current_score(my_cards)
                print(f"your cards: {my_cards}, current score: {sum_my_cards}")
                print(f"computer's first card: {dealer_cards[0]} ")
            else:                                                               # deals with person choosing to pass, calls the dealer function to add all of his cards and breaks the loop
                dealer_cards = draw_cards_dealer(dealer_cards,dealer_sum)
                dealer_sum = current_score(dealer_cards)
                print(f"Your final hand: {my_cards}, final score: {sum_my_cards}")
                print(f"Computer's final hand: {dealer_cards}, final score: {dealer_sum}")
                break
        if  sum_my_cards >21:                                                           # solves what happens when a players score is greater than 21
            print(f"Your final hand: {my_cards}, final score: {sum_my_cards}")
            dealer_cards = draw_cards_dealer(dealer_cards,dealer_sum)
            dealer_sum = current_score(dealer_cards)
            print(f"Computer's final hand: {dealer_cards}, final score: {dealer_sum}")
            print("you went over, you lose.")
            main()
        else:                                                               #checks who won if the player's sum is not above 21
            if dealer_sum > 21:                                                          
                print("computer went over, you win")
            elif dealer_sum > sum_my_cards:
                print("you lose")
            elif dealer_sum < sum_my_cards:
                print("yow win!")
            elif dealer_sum ==sum_my_cards:
                print("its a draw")
        main()

        

main()
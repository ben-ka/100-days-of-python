import art
import os

def main():
    print (art.logo)
    bidders ={}
    biggest_bid = 0
    biggest_bidder_name =""
    while True:
        name_inp = input("what is you name? \n")
        price_inp =int(input("what is your bid? \n$"))
        bidders[name_inp] = price_inp
        more_bidders  = input("is there another bidder? (yes/no) ").lower()
        if more_bidders =="yes":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif more_bidders=="no":
            break
    for bidder in bidders:
        if bidders[bidder] >biggest_bid:
            biggest_bid = bidders[bidder]
            biggest_bidder_name =bidder

    print(f"the biggest bidder is {biggest_bidder_name} with a bid of ${biggest_bid}")
    
main() 
import random
def draw_rock() :
   print("computer picked rock")
def draw_paper():
   print("computer picked paper")
def draw_scisors():
   print("computer picked scisors")
def winner(comp_choice,chosen):
    if chosen ==0 and comp_choice=="scisors":
       return("you won!")
    elif chosen==0 and comp_choice=="rock":
       return("no one wins")
    if chosen==0 and comp_choice=="paper":
       return"computer won"
    
    if chosen ==1 and comp_choice=="rock":
       return("you won!")
    elif chosen==1 and comp_choice=="paper":
       return("no one wins")
    if chosen==1 and comp_choice=="scisors":
       return"computer won"
    
    if chosen ==2 and comp_choice=="paper":
       return("you won!")
    elif chosen==2 and comp_choice=="scisors":
       return("no one wins")
    if chosen==2 and comp_choice=="rock":
       return"computer won"
    




def main():
   
    chosen = int(input("what do you choose? 0 for rock, 1 for paper or 2 for scisors ") )
    possible_choises = ["rock","paper","scisors"]
    comp_choice = random.choice(possible_choises)
    if comp_choice=="rock":
        draw_rock()
    elif comp_choice=="paper":
        draw_paper()
    elif comp_choice == "scisors":
        draw_scisors()
      
    print(winner(comp_choice,chosen))
    user_inp =  input("do you want to play again? (y/n)")
    if user_inp=="y" or user_inp=="Y":
       main()
    
       
    


main()
import random
import hangman_words
import hangman_arts

def main():
    stages = hangman_arts.stages

    j= 0 
    lives = 6
    display = []
    chosen_word = generate_word()
    print(hangman_arts.logo)
    for letter in chosen_word:
        display.append("__  " )    # adding underscores as the length of the word
    is_word_full = False
    while is_word_full ==False and lives>0:
        print(stages[lives])
        user_guess = take_letter()
       
        checking_letter(chosen_word,display , lives,user_guess)         # calling function to check inputted letter
        while j < len(display):
            if display[j] == "__  " :     # checking if there are any more underscores or letters only
                break
            j+=1 
        if j ==len(display) :         # checking if victory is achieved
            is_word_full = True
        is_letter_correct = checking_letter_correct(user_guess,chosen_word)
        
        if  is_letter_correct ==False:
            lives -=1
            print()
            print("letter does not appear in the word ")
    if is_word_full ==True:
        print()
        print("congratulations you won!!!")
    if lives ==0:
        print(stages[0])
        print("you lost")
        print(f"the correct word was {chosen_word} ")
            


def generate_word():
   word_list = hangman_words.word_list
   chosen_word = random.choice(word_list)
   return chosen_word

def take_letter():
    user_guess = input("guess a letter: ")               # user guesses a letter
    user_guess = user_guess.lower()
    return user_guess

def checking_letter(chosen_word,display,lives,user_guess ):
    
    i = 0    
    for letter in  chosen_word:
        if user_guess ==letter:                  # adds the guess to the correct place in the word instead of underscores
            display[i] = letter  +" "
           
        i+=1
    for pos in display:
        print(pos,end="   ")

   
    
def checking_letter_correct(user_guess,chosen_word):
     is_letter_correct =False
     for letter in  chosen_word:
        if user_guess ==letter:               
            is_letter_correct =True
     if is_letter_correct ==False:
        return False
     else:
         return True

main()
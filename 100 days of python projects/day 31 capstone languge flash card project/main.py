import pandas
from tkinter import *
import random
from tkinter import messagebox
import json
##### constants

SECONDS = 4
WIDTH = 1200
HEIGHT = 1000
FONT_NAME = "Courier"
FONT_SIZE = 24
BACKGROUND_COLOR = "#9dc6e9"
SECONDARY = "#55f5a0"

is_flipped = False
## window setup
window = Tk()
window.title('Learn Spanish!')
window.minsize(WIDTH,HEIGHT)
window.config(bg=BACKGROUND_COLOR,padx=WIDTH/7,pady=HEIGHT/10)

#csv to dictionary

csv_data = pandas.read_csv('data.csv')
spanish_words = csv_data['Spanish'].tolist()
english_words = csv_data["English"].tolist()
dict_data = {spanish_words[i] : english_words[i] for i in range(len(spanish_words))}

with open('data.json','w') as json_data:
    json.dump(dict_data,json_data,indent=4)


# generating random spanish word

def GenerateSpanish():
    global dict_data
    try:
        i = random.choice(list(dict_data.keys()))
    except IndexError:
        messagebox.showinfo(title='Out of Words',message='There are no more words left')

    else:
        return i
   



## get translation
def GenerateEnglish(spa_word):
    global dict_data
    return dict_data[spa_word]


# logic after swap
def SwapCard(word):
    global is_flipped
    is_flipped = True
    back_img = PhotoImage(file='images\card_back.png')
    canvas.itemconfig(card_side,image = back_img)
    canvas.config(bg=SECONDARY)
    canvas.itemconfig(language,text = 'English')
    english_word = GenerateEnglish(word)
    canvas.itemconfig(word_shown,text = english_word)


def RightMark():
    global spanish_word
    global dict_data
    global is_flipped
    if is_flipped == True:
        dict_data.pop(spanish_word)
        FrontSide()

def WrongMark():
    global spanish_word
    global dict_data
    global is_flipped
    if is_flipped == True:
        dict_data[spanish_word] = dict_data[spanish_word]
        FrontSide()



# ##setting up buttons
right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img,command=RightMark)
right_button.grid(row = 1,column=0)

wrong_img = PhotoImage(file='images\wrong.png')
wrong_button = Button(image=wrong_img,command=WrongMark)
wrong_button.grid(row=1,column=1)


#setting up canvas
def FrontSide():
    global is_flipped
    is_flipped = False
    global canvas
    global card_side
    global language
    global word_shown
    global spanish_word 
    canvas = Canvas(width=WIDTH/1.5,height=HEIGHT/1.5,highlightthickness=0,bg="#ffffff")
    front_img = PhotoImage(file="images\card_front.png")
    card_side = canvas.create_image(WIDTH/3,HEIGHT/3,image = front_img)
    spanish_word = GenerateSpanish()
    word_shown = canvas.create_text(WIDTH/3,HEIGHT/3,text=f'{spanish_word}',font=(FONT_NAME,int(FONT_SIZE*2),'bold'))
    language = canvas.create_text(WIDTH/3,HEIGHT/6,text='Spanish',font=(FONT_NAME,int(FONT_SIZE*1.3),'italic'))
    flip = window.after(SECONDS*1000,SwapCard,spanish_word)
    canvas.grid(row=0,column=0,columnspan=2)



FrontSide()
















window.mainloop()





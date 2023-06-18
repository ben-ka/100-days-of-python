
import pandas
from tkinter import *
import random
from tkinter import messagebox
import json
import pyperclip
##### constants

SECONDS = 6
WIDTH = 1400
HEIGHT = 1000
FONT_NAME = "Courier"
FONT_SIZE = 24
BACKGROUND_COLOR = "#9dc6e9"
SECONDARY = "#55f5a0"


count_true = 0
count_all = 0



is_flipped = False
## window setup
window = Tk()
window.title('Learn Spanish!')
window.minsize(WIDTH,HEIGHT)
window.config(bg=BACKGROUND_COLOR,padx=WIDTH/20,pady=HEIGHT/10)

#csv to dictionary
# asks the user if he wants to continue his previous run
if messagebox.askyesno(title='Continue previous run',message='Do you wish to continue your previous run'):
    csv_data = pandas.read_csv('new_data.csv')
else:
    csv_data = pandas.read_csv('data.csv')
spanish_words = csv_data['Spanish'].tolist()
english_words = csv_data["English"].tolist()
dict_data = {spanish_words[i] : english_words[i] for i in range(len(spanish_words))}

with open('data.json','w') as json_data:
    json.dump(dict_data,json_data,indent=4)
    

# generating random spanish word

def GenerateSpanish():
    global dict_data
    i = ''
    try:
        i = random.choice(list(dict_data.keys()))
    except IndexError:
        messagebox.showinfo(title='Out of Words',message='There are no more words left')

    else:
        pyperclip.copy(i)
        return i
   



## get translation
def GenerateEnglish(spa_word):
    global dict_data
    return f'{dict_data[spa_word]}'


# logic after swap
def SwapCard(word):
    global is_flipped
    is_flipped = True
    back_img = PhotoImage(file='images\card_back.png')
    canvas.itemconfig(card_side,image = back_img)
    canvas.config(bg=SECONDARY)
    canvas.itemconfig(language,text = word)
    english_word = GenerateEnglish(word)
    canvas.itemconfig(word_shown,text = english_word)


def RightMark():
    global spanish_word
    global dict_data
    global is_flipped
    global flip
    global count_true
    global count_all 
    count_true += 1
    count_all+=1
    Counter()
    
    dict_data.pop(spanish_word)
    window.after_cancel(flip)
    
    FrontSide()

def WrongMark():
    global spanish_word
    global dict_data
    global is_flipped
    global count_true
    global count_all 
    if is_flipped == True:
        dict_data[spanish_word] = dict_data[spanish_word]
        count_all+=1
        Counter()
        FrontSide()

# added counter to count user words



count_label = Label(text=f'{count_true} / {count_all}',font=(FONT_NAME,int(FONT_SIZE * 1.4),'italic'),bg=BACKGROUND_COLOR)
count_label.grid(row=0,column=0)

def Counter():
    if count_all >= 10:
        window.config(padx=WIDTH/40)
    if count_all >=100:
        window.config(padx=WIDTH/70)
    count_label.config(text=f'{count_true} / {count_all}')





# ##setting up buttons
right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img,command=RightMark)
right_button.grid(row = 2,column=1)

wrong_img = PhotoImage(file='images\wrong.png')
wrong_button = Button(image=wrong_img,command=WrongMark)
wrong_button.grid(row=2,column=2)


#setting up canvas
def FrontSide():
    global is_flipped
    is_flipped = False
    global canvas
    global card_side
    global language
    global word_shown
    global spanish_word 
    global flip
    canvas = Canvas(width=WIDTH/1.5,height=HEIGHT/1.5,highlightthickness=0,bg="#ffffff")
    front_img = PhotoImage(file="images\card_front.png")
    card_side = canvas.create_image(WIDTH/3,HEIGHT/3,image = front_img)
    spanish_word = GenerateSpanish()
    word_shown = canvas.create_text(WIDTH/3,HEIGHT/3,text=f'{spanish_word}',font=(FONT_NAME,int(FONT_SIZE*2),'bold'))
    language = canvas.create_text(WIDTH/3,HEIGHT/7,text='Spanish',font=(FONT_NAME,int(FONT_SIZE*1.6),'italic'))
    canvas.create_line(-WIDTH/10,HEIGHT/6,WIDTH,HEIGHT/6,width=3)
    flip = window.after(SECONDS*1000,SwapCard,spanish_word)
    canvas.grid(row=1,column=1,columnspan=2,padx=5,pady=5)



FrontSide()



# on window close it saves the progress on another file


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        global dict_data
        new_data = pandas.DataFrame.from_dict(dict_data,orient='index')
        new_data.reset_index(inplace=True)
        new_data.columns = ['Spanish', 'English']
        new_data.to_csv('new_data.csv', index=False)

            
                


window.protocol("WM_DELETE_WINDOW", on_closing)










window.mainloop()





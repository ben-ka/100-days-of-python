from tkinter import *

#  constants

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

WIDTH = 500
HEIGHT = 500
FONT_SIZE = 34

CENTER_WIDTH = WIDTH/2 - WIDTH/70

CHECK_MARK = '✔'
######

reps = 0
timer = None

# countdown
def Countdown(minutes,seconds):
    global reps
    global timer
    state.config(text='Work')
    if minutes >= 0 and seconds >= 0:
        canvas.itemconfig(main_timer, text=f"{minutes:02d}:{seconds:02d}")
        if seconds > 0:
           timer =  window.after(1000, Countdown, minutes, seconds - 1)
        else:
            timer = window.after(1000, Countdown, minutes - 1, 59)
   
    elif reps < 3:
        reps+=1
        Break(SHORT_BREAK_MIN,0)
        
    
    elif reps == 3:
        reps = 0
        Break(LONG_BREAK_MIN,0)
        
    

def Break(minutes,seconds):
    global reps
    global timer
    state.config(text='Rest')
    if minutes >= 0 and seconds >= 0:
        canvas.itemconfig(main_timer, text=f"{minutes:02d}:{seconds:02d}")
        if seconds > 0:
           timer =  window.after(1000, Break, minutes, seconds - 1)
        else:
            timer = window.after(1000, Break, minutes - 1, 59)
    else:      
        mark.config(text=CHECK_MARK*reps)
        Countdown(WORK_MIN,0)



# window
window = Tk()
window.minsize(WIDTH,HEIGHT)
window.title('pomodoro app')
window.config(bg=YELLOW,padx=200,pady=100)


# label heading
state = Label(text='TIMER')
state.configure(fg=GREEN,font=(FONT_NAME,2 * FONT_SIZE,'italic'),bg=YELLOW)
state.grid(column=1,row=0)

#check mark label

mark = Label(text='')
mark.config(fg=GREEN,bg=YELLOW,font=(FONT_NAME,FONT_SIZE,'italic'))
mark.grid(column=1,row=3)

# start button
def OnStartButtonPress():
    Countdown(WORK_MIN,0)
    

start_button = Button(text='Start', font=(FONT_NAME,int(FONT_SIZE/2),'italic'),pady=5,command=OnStartButtonPress)
start_button.grid(column=0,row=2)


# reset button
def OnRestButtonPress():
    global reps
    global timer
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(main_timer, text='00:00')
    state.config(text='TIMER')
    mark.config(text='')
    


reset_button = Button(text='Reset',font=(FONT_NAME,int(FONT_SIZE/2),'italic'),pady=5,command=OnRestButtonPress)
reset_button.grid(column=2,row=2)

# canvas including timer and tomato pic
canvas = Canvas(width=WIDTH,height=HEIGHT,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(CENTER_WIDTH ,HEIGHT/2.25,image = tomato_img )
main_timer = canvas.create_text(CENTER_WIDTH , HEIGHT/2.12,text='00:00',font=(FONT_NAME,FONT_SIZE,'italic'), fill='White')


#canvas.create_text(CENTER_WIDTH, HEIGHT/8, text = 'TIMER',font=(FONT_NAME,2 * FONT_SIZE,'italic'), fill=GREEN )

canvas.grid(column=1,row=1)
















window.mainloop()

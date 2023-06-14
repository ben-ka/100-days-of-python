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

WIDTH = 1300
HEIGHT = 800
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
window.config(bg=YELLOW,padx=150,pady=100)


# label heading
state = Label(text='TIMER')
state.configure(fg=GREEN,font=(FONT_NAME,2 * FONT_SIZE,'italic'),bg=YELLOW)
state.grid(column=3,row=0)


#scale 1 - work minutes
def Work_scale_used():
    global WORK_MIN
    WORK_MIN = work_min_scale.get()
    OnStartButtonPress(int(work_min_scale.get()))
    

work_min_scale = Scale(from_=0,to=60,bg=RED)
work_min_scale.config(width=20)
work_min_scale.set(value=WORK_MIN)
work_min_scale.grid(column=2,row=2)


#scale 2 - small break

def Small_break_scale_used(value):
    global SHORT_BREAK_MIN
    SHORT_BREAK_MIN = rest_min_scale.get()

rest_min_scale = Scale(from_=0,to=60,command=Small_break_scale_used,bg=RED)
rest_min_scale.config(width=20)
rest_min_scale.set(value=SHORT_BREAK_MIN)
rest_min_scale.grid(column=1,row=2)


#scale 3 - long break
def long_break_scale_used(value):
    global LONG_BREAK_MIN
    LONG_BREAK_MIN = long_rest_min_scale.get()

long_rest_min_scale = Scale(from_=0,to=60,command=long_break_scale_used,bg=RED)
long_rest_min_scale.config(width=20)
long_rest_min_scale.set(value=LONG_BREAK_MIN)
long_rest_min_scale.grid(column=0,row=2)


#label 1 - work minutes
label_work_min = Label (text = 'Work Minutes', font=(FONT_NAME,int(FONT_SIZE/3),'italic'),fg=PINK,bg=YELLOW)
label_work_min.grid(column=2,row=1)


#label 2 - rest minutes
label_rest_min = Label (text = 'Short Rest Minutes', font=(FONT_NAME,int(FONT_SIZE/3),'italic'),fg=PINK,bg=YELLOW,padx=15)
label_rest_min.grid(column=1,row=1)


#label 3 - long rest minutes
label_long_rest_min = Label (text = 'Long Rest Minutes', font=(FONT_NAME,int(FONT_SIZE/3),'italic'),fg=PINK,bg=YELLOW)
label_long_rest_min.grid(column=0,row=1)





#check mark label

mark = Label(text='')
mark.config(fg=GREEN,bg=YELLOW,font=(FONT_NAME,FONT_SIZE,'italic'))
mark.grid(column=3,row=5)

# start button
def OnStartButtonPress(minutes):
   Countdown(minutes,0)
    
    

start_button = Button(text='Start', font=(FONT_NAME,int(FONT_SIZE/2),'italic'),pady=5,command=Work_scale_used)
start_button.grid(column=2,row=4)


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
reset_button.grid(column=4,row=4)

# canvas including timer and tomato pic
canvas = Canvas(width=WIDTH,height=HEIGHT,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(CENTER_WIDTH ,HEIGHT/2.25,image = tomato_img )
main_timer = canvas.create_text(CENTER_WIDTH , HEIGHT/2.12,text='00:00',font=(FONT_NAME,FONT_SIZE,'italic'), fill='White')


#canvas.create_text(CENTER_WIDTH, HEIGHT/8, text = 'TIMER',font=(FONT_NAME,2 * FONT_SIZE,'italic'), fill=GREEN )

canvas.grid(column=3,row=3)




window.mainloop()

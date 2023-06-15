from tkinter import *
from tkinter import messagebox
from password_generator_logic import Generate
import pyperclip

#constants
WIDTH = 800
HEIGHT = 800
FONT_NAME = "Courier"
FONT_SIZE = 24



#window

window = Tk()
window.minsize(WIDTH,HEIGHT)
window.title('Password Manager')
window.config(padx=WIDTH/10,pady=HEIGHT/20)

#canvas
canvas = Canvas(width=WIDTH/2,height=HEIGHT/2,highlightthickness=20)
password_img = PhotoImage(file='logo.png')
canvas.create_image(WIDTH/4,HEIGHT/3,image = password_img)
canvas.grid(column=1,row=0)


# entries

#website entry
website_label = Label(text='Website: ',font=(FONT_NAME,FONT_SIZE,'italic'))
website_label.grid(column=0,row=1)

website_selected = Entry(width=int(WIDTH/9))
website_selected.config(font=(FONT_NAME,int(FONT_SIZE/1.85)))
website_selected.grid(column=1,row=1,ipady=10,columnspan=2,pady=20)


#function to check if the website is alradey entered
def IS_website_ava():
    name = website_selected.get()
    with open ('passwords.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            if name in line:
                return False
        return True


# username entry

username_label = Label(text='Email/Username: ',font=(FONT_NAME,FONT_SIZE,'italic'))
username_label.grid(column=0,row=2)

username_selected = Entry(width=int(WIDTH/9))
username_selected.config(font=(FONT_NAME,int(FONT_SIZE/1.85)))
username_selected.grid(column=1,row=2,ipady=10,columnspan=2)


# password entry

password_label = Label(text='Password: ',font=(FONT_NAME,FONT_SIZE,'italic'))
password_label.grid(column=0,row=3)



password_selected = Entry(width=int(WIDTH/13.2))
password_selected.config(font=(FONT_NAME,int(FONT_SIZE/1.85)))
password_selected.grid(column=1,row=3,ipady=10)

#generate password button
def Generate_button_pressed():
    generated_password = ''
    generated_password = Generate()
    pyperclip.copy(generated_password)
    password_selected.delete(0,END)
    password_selected.insert(0,generated_password)
    

generate_password = Button(text = 'Generate password',font=(FONT_NAME,int(FONT_SIZE/1.3),'italic'),command=Generate_button_pressed)
generate_password.grid(column=2,row=3,pady=20,padx=10)


#add button
def OnAddButtonPressed():
    with open('passwords.txt','a') as passwords_saved:
        if IS_website_ava() == True :
            complete = f'{website_selected.get()}  || {username_selected.get()}  || {password_selected.get()}'
            passwords_saved.write(complete)
            passwords_saved.write('\n\n')
        else:
            messagebox.showerror(title='Error',message='Website already exists in password manager')
            
        


add_button = Button(text = 'Add',font=(FONT_NAME,int(FONT_SIZE),'italic'),command=OnAddButtonPressed,width=int(WIDTH/50))
add_button.grid(column=1,row=5)



window.mainloop()
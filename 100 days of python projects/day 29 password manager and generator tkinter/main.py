from tkinter import *
from tkinter import messagebox
from password_generator_logic import Generate
import pyperclip
import json


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

website_selected = Entry(width=int(WIDTH/13.6))
website_selected.config(font=(FONT_NAME,int(FONT_SIZE/1.85)))
website_selected.grid(column=1,row=1,ipady=10,columnspan=1,pady=20)


# search for a website and get details

def GetDetailsFromWebsite():
    website = website_selected.get()
    is_there = True
    try:
        with open('passwords.json','r') as file1 :
            data = json.load(file1)
        try:
            details = data[website]
        except KeyError:
            is_there =False
        else:
            password = details['Password']
            email = details['Email']
            messagebox.showinfo(title=f'{website} details', message=f'Your login data is: \nEmail/Username: {email} \n Password: {password}')
            pyperclip.copy(password)
    except FileNotFoundError:
        is_there = False
    if is_there == False:
        messagebox.showerror(message='This website name does not exist',title='Error')





search_website = Button(text='Search',font=(FONT_NAME,int(FONT_SIZE/1.3),'italic'),command=GetDetailsFromWebsite,width=19)
search_website.grid(column=2,row=1,pady=20,padx=10)

#function to check if the website is alradey entered
def IS_website_ava():
    name = website_selected.get()

    try:
        with open ('passwords.json','r') as file1:
            data = json.load(file1)
            try:
                data[name] = data[name]
            except KeyError:
                return True
            else:
                return False
    except FileNotFoundError:
        return True


# checks if all the entries have been filled
def Entries_ok():
    if len(website_selected.get()) > 0 and len(username_selected.get()) > 0  and len(password_selected.get()) > 0:
        return True
    return False





# username entry

username_label = Label(text='Email/Username: ',font=(FONT_NAME,FONT_SIZE,'italic'))
username_label.grid(column=0,row=2)

username_selected = Entry(width=int(WIDTH/9))
username_selected.config(font=(FONT_NAME,int(FONT_SIZE/1.85)))
username_selected.grid(column=1,row=2,ipady=10,columnspan=2)


# password entry

password_label = Label(text='Password: ',font=(FONT_NAME,FONT_SIZE,'italic'))
password_label.grid(column=0,row=3)



password_selected = Entry(width=int(WIDTH/13.6))
password_selected.config(font=(FONT_NAME,int(FONT_SIZE/1.85)))
password_selected.grid(column=1,row=3,ipady=10)

#generate password button
def Generate_button_pressed():
    generated_password = ''
    generated_password = Generate()
    pyperclip.copy(generated_password)
    password_selected.delete(0,END)
    password_selected.insert(0,generated_password)
    

generate_password = Button(text = 'Generate password',font=(FONT_NAME,int(FONT_SIZE/1.3),'italic'),command=Generate_button_pressed,width=19)
generate_password.grid(column=2,row=3,pady=20,padx=10)


#add button
def OnAddButtonPressed():
    website = website_selected.get()
    email = username_selected.get()
    password = password_selected.get()


    is_webstie_aval = IS_website_ava()
    entries_good = Entries_ok()
    if  is_webstie_aval == True :
        if entries_good == True : 
            new_data = {website :
                        {'Email' : email,
                        'Password' : password},                             
                        } 
            with open('passwords.txt','w') as passwords_saved:
                complete = f'{website_selected.get()}  | {username_selected.get()}  | {password_selected.get()}'
                passwords_saved.write(f'{complete}\n\n')

            try:   
                with open('passwords.json','r') as passwords_saved:
                # reading old data off json
                    data = json.load(passwords_saved)
                    # updating new data into old data           

            except FileNotFoundError:
                with open('passwords.json','w') as file1:
                    json.dump(new_data,file1,indent=4)

            else:
                data.update(new_data) 
                with open('passwords.json','w') as passwords_saved:
            # writing the updated data into json
                    json.dump(data,passwords_saved,indent=4)

            

            

        
        else:
            messagebox.showerror(title= 'Error',message='Not all fields are registered \nPlease fill the missing entries')
        
            
    else:
        messagebox.showerror(title='Error',message='Website already exists in password manager')
    
    username_selected.delete(0,END)
    password_selected.delete(0,END)
    if entries_good == True:
        website_selected.delete(0,END)
            
        


add_button = Button(text = 'Add',font=(FONT_NAME,int(FONT_SIZE),'italic'),command=OnAddButtonPressed,width=int(WIDTH/50))
add_button.grid(column=1,row=5)



window.mainloop()

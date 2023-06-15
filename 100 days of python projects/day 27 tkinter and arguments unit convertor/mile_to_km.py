from tkinter import *

FONT = ('Arial',24)
window = Tk()
window.title('mile to km converter')
window.minsize(width=200,height=200)

def radio_used():
   print(radio_state.get())
   if radio_state.get() ==2:
      label1.config(text='Km')
      label4.config(text='miles')
   if radio_state.get() == 1:
      label1.config(text='miles')
      label4.config(text='km')
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="mile to km", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="km to mile", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=1,row=3)
radiobutton2.grid(column=1,row=4)



mile_input = Entry()
mile_input.grid(column=1,row=0)




label1 = Label(text='miles',font=FONT)

label1.grid(column=2,row=0)


km = 0
miles = 0
label2 =  Label(text=f'is equal to ', font=FONT)
label2.grid(column=0, row=1)

label3 = Label(text=f'{km}',font=FONT)
label3.grid(column=1,row=1)

label4 =Label(text='km',font=FONT)
label4.grid(column=2,row=1)

def On_button_press():
   
   direction = radio_state.get()
   if direction !=2:
      km = mile_input.get() 
      label3.config(text=f'{round(float(km)*1.6)}',font=FONT)
   else:
      miles = mile_input.get()
      label3.config(text=f'{round(float(miles)/1.6)}',font=FONT)


button = Button(text='calculate',command=On_button_press)
button.grid(column=1,row=2)









window.mainloop()

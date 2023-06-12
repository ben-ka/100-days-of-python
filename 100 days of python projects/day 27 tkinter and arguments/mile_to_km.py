from tkinter import *
window = Tk()
window.title('mile to km converter')
window.minsize(width=100,height=100)

mile_input = Entry()
mile_input.grid(column=1,row=0)

label1 = Label(text='miles')
label1.grid(column=2,row=0)

km = 0
label2 =  Label(text=f'is equal to {km} km')
label2.grid(column=0, row=1)

def On_button_press():
   km = mile_input.get() 
   
   label2.config(text=f'is equal to {int(float(km)*1.6)} km')

button = Button(text='calculate',command=On_button_press)
button.grid(column=1,row=2)





window.mainloop()
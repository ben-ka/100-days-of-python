
import tkinter

window = tkinter.Tk()
window.title('test')
window.minsize(800,800)
window.config(padx=100,pady=300)


#label
my_label = tkinter.Label(font=('Arial',24))
my_label['text'] = 'hello worlddd'
my_label.grid(column=0,row=0)

#button
def On_button_click():
    my_label['text'] = user_inp.get()

button = tkinter.Button(text='click me',font=('Arial',24),command=On_button_click)
button.grid(column=1,row=1)

new_button = tkinter.Button(text='click him',font=('Arial',24))
new_button.grid(column=2,row=0)


#entry
user_inp = tkinter.Entry(width = 20)
user_inp.grid(column=3,row=2)

window.mainloop()



# def add(*args):
#     n=0
#     for arg in args:
#         n+=arg
#     print(n)

# def calc(n, **kwargs):
#     print(kwargs)
#     # for key,value in kwargs.items():       
#     #     print(value)
#     # print(kwargs['add'])
#     x = n+kwargs['add']*kwargs['multiply']
#     print(x)


# calc(2, add=3,multiply=5)

# add(2,12,13,5,3,56,7,8,8,9)


# class Car:
#     def __init__(self,**kwargs):
#         self.make=kwargs.get('make')
#         self.model = kwargs.get('model')
# my_car = Car(make = 'make car')
# print(my_car.model)
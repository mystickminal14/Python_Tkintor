from tkinter import *

window = Tk()
count = 0

def increment():
    global count
    count += 1
    label.config(text=count)
    if count == 10:
        button.config(state=DISABLED)
    else:
        button.config(state='normal')
    button2.config(state='normal') 

def decrease():
    global count
    count -= 1
    label.config(text=count)
    if count == 0:
        button2.config(state=DISABLED)
        label2.config(text='You can\'t decrement from here on out')
    else:
        button.config(state='normal')  

label = Label(window,
             text=0,
             fg='black',
             bg='gray',
             font=('Comic Sans', 45, 'bold'))

label.place(x=20, y=20)

label2 = Label(window,
              text='',
              fg='black',
              bg='gray',
              font=('Comic Sans', 14, 'bold'))  

label2.place(x=50, y=70)  # Adjusted the y-coordinate

button = Button(window,
                text='Increment',
                relief=RAISED,
                bd=5,
                font=('arial', 16, 'bold'),  
                activeforeground='blue',
                activebackground='black',
                fg='red',
                bg='black',
                command=increment)

button.place(x=20, y=100)

button2 = Button(window,
                 text='Decrement',
                 relief=RAISED,
                 bd=5,
                 font=('arial', 16, 'bold'),  
                 activeforeground='blue',
                 activebackground='black',
                 fg='red',
                 bg='black',
                 command=decrease)

button2.place(x=180, y=100)

window.geometry('400x200')  # Adjusted window size
window.iconphoto(True, PhotoImage(file='cream.png'))
window.config(background='gray')
window.mainloop()

from tkinter import *

window= Tk()

photo=PhotoImage(file='cream.png')
label=Label(window,text="My name is minal",
            font=('IMPACT',20,'bold'),
            fg='white',
            bg='BLACK',
            relief=RAISED,
            bd=5,
            padx=50,
            pady=50,
            image=photo,
            compound='bottom')
label.place(x=50,y=50)



window.title('label')
window.geometry("400x400")
window.config(background="#AAD177")
window.mainloop()
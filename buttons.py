from tkinter import *

window=Tk()

button=Button(window,text='Click me',
                font=('comic sans',11,'bold'),
              fg='white',
              bg='black',
              activeforeground='white',
              activebackground='black',
              relief='flat',
              
              height=1,
              width=8
              
              )
button.place(x=20,y=20)

window.config(background='#7B8B99')
window.geometry("400x400")
window.mainloop()
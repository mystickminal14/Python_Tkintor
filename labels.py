from tkinter import *

window= Tk()

icon=                                                                                                                                                                                                                                                                                                                                                                              (file='cream.png')
label=Label(window,text="firstname",
            font=('IMPACT',20,'bold'),
            fg='white',
            bg='BLACK',
            relief=RAISED,
            bd=5,
            padx=50,
            pady=50,
            image=icon,
            
            compound='bottom')
label.place(x=50,y=50)



window.title('label')
window.geometry("400x400")
window.config(background="#AAD177")
window.mainloop()
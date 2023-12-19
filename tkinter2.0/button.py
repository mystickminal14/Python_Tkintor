from tkinter import *
window=Tk()
def click():
    print("clicked")
    label44.config(text="this is sheesh")



label=Label(window,text="This is a button",font=('arial',55,'underline'),relief=RAISED,fg='blue',bg='yellow',padx=5,pady=5)
label.place(x=10,y=10)
image=PhotoImage(file="cream.png")

label44=Label(window,text='')
label44.place(x=10,y=120)
button=Button(window,text='Click me',font=("Comic Sans",30),bg='blue',fg='yellow',image=image,compound='bottom', relief=SUNKEN,bd=10,command=click, activeforeground='red',activebackground="blue")
button.place(x=10,y=250)
window.iconphoto(True,PhotoImage(file='cream.png'))
window.geometry("800x800")
window.config(background='gray')
window.mainloop()
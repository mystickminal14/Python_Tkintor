from tkinter import *
window=Tk()
def delete_text():
   entry.delete(0, END)


def submit():
    user = entry.get()
    label.config(text=user)
def backspace():
    entry.delete(len(entry.get())-1,END)


label=Label(window,
            text='',
           bg='gray' )
label.place(x=100,y=100)
entry=Entry(window,
            font=('Arial',20),
            relief=SUNKEN,
            bd=4,
            show='*'
            )
entry.insert(0,'minal')
entry.place(x=20,y=50)
button=Button(window,
              text="SUBMIT",
              command=submit)
button.place(x=350,y=60)
button2=Button(window,
              text="DELETE",
              command=delete_text)
button2.place(x=400,y=60)
button3=Button(window,
              text="BACKSPACE",
              command=backspace)
button3.place(x=450,y=60)
window.iconphoto(True,PhotoImage(file='cream.png'))
window.config(background='gray')
window.geometry('600x600')
window.mainloop()
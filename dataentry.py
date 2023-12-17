from tkinter import *
def submit():
    username =entry.get()
    print("hellow",username)
window=Tk()
entry=Entry(window,
            font=('Arial',50))
entry.pack(side=LEFT)
submit=Button(window,text='submit'
              ,command=submit)
submit.place(x=10,y=100)
window.geometry('400x400')
window.mainloop()
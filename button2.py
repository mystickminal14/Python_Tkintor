from tkinter import *

num = 10

def show():
    global num
    num = num - 1
    lab.config(text=str(num))
    if num == 0:
        hbd.config(text="Happy Birthday Sparsha!!")

win = Tk()
hbd = Label(win, text='')
hbd.pack()
lab = Label(win, text='')
lab.pack()

button = Button(win, text='Click me', command=show)
button.pack()

win.geometry('300x300')
win.mainloop()

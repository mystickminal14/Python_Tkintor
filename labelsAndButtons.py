from tkinter import *

window= Tk()
pic=PhotoImage(file='cream.png')
resized_pic = pic.subsample(5)
label=Label(window,text="User name 👤:",
            fg='white',
            bg='black',
            font=('comic sans',10,'bold'),
            
            compound='right'
            )
label.place(x=40,y=40)

button=Button(window,text='click me',
              fg='white',
              bg='black',
            
              compound='right')
button.pack()
label=Label(window,image=pic)
label.pack()
window.geometry("600x600")
window.config(background='black')
window.mainloop()
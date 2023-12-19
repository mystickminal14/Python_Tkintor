from tkinter import *
window=Tk()
img=PhotoImage(file="cream.png")

label1=Label(window,text="MY NAME IS MINAL",font=('Arial',40,'bold'),fg='red',bg='skyblue',relief=RAISED,bd=10,padx=20,pady=20)
label1.place(x=100,y=100)

window.iconphoto(True,img)
window.title("this is great minal")
window.geometry('400x400')
window.config(background='skyblue')
window.mainloop()
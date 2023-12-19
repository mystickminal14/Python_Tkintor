from tkinter import *
 
register=Tk()
icon=PhotoImage(file="cream.png")

register.config(background='darkgray')
register.iconphoto(True,icon)
register.title("Minal first gui program")
register.geometry("420x420")
register.mainloop()
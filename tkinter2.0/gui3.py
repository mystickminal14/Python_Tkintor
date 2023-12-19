from tkinter import *

window = Tk()

label = Label(window,
              text="This image name is crochet by takri",
              relief=SUNKEN,
              padx=10,
              pady=10,
              fg='yellow',
              bg='gray',
              font=('league gothic', 10, 'underline'),  # Adjusted font size
              image=PhotoImage(file="cream.png"),
              compound='bottom'
              )

window.iconphoto(True, PhotoImage(file="cream.png"))  # Corrected method name
window.title("Great you are back minal")
window.geometry('800x800')
window.config(background='gray')

label.pack()  # Pack the label into the window
window.mainloop()

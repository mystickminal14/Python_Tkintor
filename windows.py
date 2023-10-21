from tkinter import *
#windows serves as container  to hold or contain widget
#widgets=gui elements likebutton,textboxes,labels and images

window=Tk() #instatiate an instance of window
window.title("First Gui")
icon=PhotoImage(file='cream.png')
window.geometry("400x400")
window.iconphoto(True,icon)
window.config(background="#AAD177")
window.mainloop()




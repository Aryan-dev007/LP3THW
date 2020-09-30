from tkinter import *

root = Tk()

def Click():
    mylabel = Label(root, text="You just clicked the button")
    mylabel.pack()

mybutton = Button(root, text="Click me", padx=50,pady=50, command=Click,fg="blue", highlightbackground="red")
# i don't know why instead of "bg" i have to use "highlightbackground" option.
mybutton.pack()

root.mainloop()

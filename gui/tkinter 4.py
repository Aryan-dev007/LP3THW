# To use input box in tkinter we use "entry widget".

from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="Blue", fg="white", borderwidth=10)
e.pack()
e.insert(0,"Enter your name: ")

def Click():
    mylabel = Label(root, text="Hi there "+e.get())
    mylabel.pack()

mybutton = Button(root, text="What is your name?", padx=50,pady=50, command=Click,fg="blue", highlightbackground="red")
# i don't know why instead of "bg" i have to use "highlightbackground" option.
mybutton.pack()

root.mainloop()

# In this upto line 20 learned about "Entry" function and its other inputs
# e.get() function also.
# e.insert(0,"string") we use 0 here cause we only have one box i.e. Enter your name

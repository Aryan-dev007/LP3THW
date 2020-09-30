from tkinter import *

root = Tk()

e = Entry(root, fg="blue", bg="white", borderwidth=5)
e.pack()
e.insert(0, "Enter you name")

def Click():
    mylabel = Label(root, text="Hello there " + e.get()).pack()

myButton = Button(root, text="Click here", padx=10, pady=10, command=Click, fg="white",highlightbackground="blue").pack()

root.mainloop()

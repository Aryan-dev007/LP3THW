from tkinter import *
# in tkinter every thing has h widget(button widget, text widget, frame widget, root widget) Root widget is a window widget.
root = Tk()  #creating

# creating a label widget

# creating a thing in tkinter is a two step process you have to define and thing and then print up on the screen.

# creating a label widget
mylabel1 = Label(root, text="Hello World!")
mylabel2 = Label(root, text="Hi there!")

# couple of ways to put label on screen we are going to see --> gird

mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1, column=0)


# creating an invent loop
# gui is always looping (constantly)

root.mainloop()

# two widgets created upto line 23 ---> root and grid.

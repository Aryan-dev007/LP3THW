from tkinter import *
# in tkinter every thing has a widget(button widget, text widget, frame widget, root widget) Root widget is a window widget.
root = Tk()  #creating

# creating a label widget

# creating a thing in tkinter is a two step process you have to define and thing and then print up on the screen.

# creating a label widget
mylabel = Label(root, text="Hello World!")

# couple of ways to put label on screen we are going to see --> pack.

#packing it onto the screen with minimum space required by default
mylabel.pack()


# creating an invent loop
# gui is always looping (constantly)

root.mainloop()

# two widgets created upto line 23 ---> root and label

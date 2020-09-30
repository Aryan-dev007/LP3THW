from tkinter import *

root = Tk()

# creating a button widget

def myClick():
    myLabel = Label(root, text = "I just clicked the button")
    myLabel.pack()

# myButton = Button(root, text="Click me!",state=DISABLED) button is now disabled.
myButton = Button(root, text="Click me!",padx=50, pady=50,command = myClick)

#learned about command function to execute any of the functions make sure not to add ()
# since it executes the function before the click can happen
# padx and pady is for size of the button
myButton.pack() # packing the button up.
root.mainloop()

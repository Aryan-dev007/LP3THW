from tkinter import *

root = Tk()

mylabel1 = Label(root, text="Hi there").grid(row=0, column=0)
mylabel2 = Label(root, text="How are you?").grid(row=1, column=1)
mylabel3 = Label(root, text="?").grid(row=2, column=2)

# mylabel1.grid(row=0, column=0)
# mylabel2.grid(row=1, column=1)
# mylabel3.grid(row=2, column=2)
# shortening the code since python is object oriented language

root.mainloop()

"""
Project:
Author:
Date:
Description:
...

Use:
"""
from tkinter import *

# Giving a Function To The Button
def btn1():
    print("I Don't Know Your Name")

if __name__ == '__main__':
    # Creating a win
    win = Tk()
    # Creating The Button
    button1 = Button(win, text="Click Me To Print SomeThing", command=btn1)
    # put on screen
    button1.pack()
    win.mainloop()

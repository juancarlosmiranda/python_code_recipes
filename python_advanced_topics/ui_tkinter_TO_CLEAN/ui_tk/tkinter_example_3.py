import tkinter as tk
from tkinter import *


class GUI(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        #self.fnameLabel = tk.Label(master, text="First Name")
        #self.fnameLabel.grid()

        #self.fnameEntry = tk.Entry(master)
        #self.fnameEntry.grid()

        #self.lnameLabel = tk.Label(master, text="Last Name")
        #self.lnameLabel.grid()

        #self.lnameEntry = tk.Entry(master)
        #self.lnameEntry.grid()

        self.submitButton = tk.Button(master, command=self.buttonClick, text="Submit")
        self.submitButton.grid()

    def buttonClick(self):
        """ handle button click event and output text from entry area"""
        print("BUTTON CLICK!!")
        pass


if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()

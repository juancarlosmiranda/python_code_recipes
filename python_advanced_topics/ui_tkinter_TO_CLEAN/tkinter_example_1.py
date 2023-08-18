import tkinter as tk
from tkinter import *


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        self.mondialLabel = tk.Label(master, text='First example of Tk')
        self.mondialLabel.grid()

        self.enableClientsButton = tk.Button(master, command=self.not_implemented_yet, text='ENABLE REMOTE CLIENTS')
        self.enableClientsButton.grid()

        self.quitButton = tk.Button(master, command=self.quit, text='Quit')
        self.quitButton.grid()

    def not_implemented_yet(self):
        print("NOT IMPLEMENTED YET!!!")
        #texto = StringVar()
        #texto.set("Un nuevo texto")
        #self.mondialLabel.config(textvariable=texto)


if __name__ == '__main__':
    app = Application()
    app.mainloop()
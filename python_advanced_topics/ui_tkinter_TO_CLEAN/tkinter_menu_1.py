"""
pip install tk

Menus, about box and buttons
"""
import tkinter as tk


# https://www.pythontutorial.net/tkinter/tkinter-toplevel/


class AboutWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('300x100')
        self.title('About...')
        self.attributes('-topmost', True)
        aboutLabel = tk.Label(self, text='A text here')
        aboutLabel.config(bg="#00ffff", font=("Verdana", 12))
        aboutLabel.pack(anchor=tk.CENTER)
        buttonClose = tk.Button(self, text='Close', command=self.destroy).pack(expand=True)


class Application(tk.Tk):
    def __init__(self, master=None):
        super().__init__()
        # -----------------------
        self.geometry('320x480')
        self.title("A title here")
        self.resizable(width=False, height=False)
        self.attributes('-topmost', True)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        # -----------------------
        self.createWidgets()
        self.createMenuBars()

    def createWidgets(self):
        self.left_frame = tk.Frame(self)
        self.enableClientsButton = tk.Button(self.left_frame, text='Enable remote clients',
                                             command=self.not_implemented_yet)
        self.startRecordButton = tk.Button(self.left_frame, text='Start record', command=self.not_implemented_yet)
        self.stopRecordButton = tk.Button(self.left_frame, text='Stop record', command=self.not_implemented_yet)
        self.shutdownClientsButton = tk.Button(self.left_frame, text='Shutdown remote clients',
                                               command=self.not_implemented_yet)
        # ---------------
        self.left_frame.grid(row=0, column=1, sticky=tk.EW)
        self.enableClientsButton.grid(row=1, column=1, sticky=tk.EW)
        self.startRecordButton.grid(row=2, column=1, sticky=tk.EW)
        self.stopRecordButton.grid(row=3, column=1, sticky=tk.EW)
        self.shutdownClientsButton.grid(row=4, column=1, sticky=tk.EW)
        # ---------------
        self.quitButton = tk.Button(self.left_frame, text='Quit', command=self.quit_app)
        self.quitButton.grid(row=5, column=1, sticky=tk.EW)
        # ---------------

    def createMenuBars(self):
        self.menubar = tk.Menu(self)
        self.menu_help = tk.Menu(self.menubar, tearoff=False)  # delete dash lines
        self.menu_help.add_command(label='About...', command=self.not_implemented_yet)
        self.menubar.add_cascade(menu=self.menu_help, label='About', underline=0)
        self.config(menu=self.menubar)  # add menu to window

    def not_implemented_yet(self):
        print("Not implemented yet!!!")
        about_windows = AboutWindow(self)
        about_windows.grab_set()

    def quit_app(self):
        self.quit
        self.destroy()


if __name__ == '__main__':
    app = Application()
    app.mainloop()

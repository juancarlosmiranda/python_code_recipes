"""
Project:
Author:
Date:
Description:
...

Use:
"""
import tkinter as tk
# https://www.pythontutorial.net/tkinter/tkinter-toplevel/
from ui_client_config import UIClientConfig
from remote_connection import RemoteConnection
from cmd_config import CmdConfig


class AboutWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('300x100')
        self.title('About...')
        aboutLabel = tk.Label(self, text='ABOUT THIS SOFTWARE')
        aboutLabel.config(bg="#00ffff", font=("Verdana", 12))
        aboutLabel.pack(anchor=tk.CENTER)
        buttonClose = tk.Button(self, text='Close', command=self.destroy).pack(expand=True)


class UICameraManagerConsole(tk.Tk):
    connection_obj = None

    def __init__(self, master=None):
        super().__init__()
        self.geometry('300x200')
        self.title("Remote camera console")
        # calling methods to create components
        self.createWidgets()
        self.createMenuBars()
        self.ui_config_obj = UIClientConfig()
        self.connection_obj = RemoteConnection(self.ui_config_obj)
        self.connection_obj.send_set_connection()

    def createWidgets(self):
        self.enableClientsButton = tk.Button(self, text='ENABLE REMOTE CLIENTS', command=self.enable_clients)
        self.startRecordButton = tk.Button(self, text='START RECORD', command=self.enable_record)
        self.stopRecordButton = tk.Button(self, text='STOP RECORD', command=self.stop_record)
        self.shutdownClientsButton = tk.Button(self, text='SHUTDOWN REMOTE CLIENTS', command=self.shutdown_clients)
        # ---------------
        self.enableClientsButton.grid()
        self.startRecordButton.grid()
        self.stopRecordButton.grid()
        self.shutdownClientsButton.grid()
        # ---------------
        self.quitButton = tk.Button(self, text='Quit', command=self.quit_app)
        self.quitButton.grid()

    def createMenuBars(self):
        self.menubar = tk.Menu(self)
        self.menu_help = tk.Menu(self.menubar, tearoff=False)  # delete dash lines
        self.menu_help.add_command(label="About...", command=self.not_implemented_yet)
        self.menubar.add_cascade(menu=self.menu_help, label='About', underline=0)
        self.config(menu=self.menubar)  # add menu to window

    def not_implemented_yet(self):
        print("NOT IMPLEMENTED YET!!!")
        about_windows = AboutWindow(self)
        about_windows.grab_set()

    def enable_clients(self):
        print("print enable clients")
        self.connection_obj.send_remote_cmd(CmdConfig.enable_remote_client)

    def enable_record(self):
        print("print enable record")
        self.connection_obj.send_remote_cmd(CmdConfig.start_record)

    def stop_record(self):
        print("stop record")
        self.connection_obj.send_remote_cmd(CmdConfig.stop_record)

    def shutdown_clients(self):
        print("shutdown clients")
        self.connection_obj.send_remote_cmd(CmdConfig.stop_remote_client)

    def quit_app(self):
        # ---------------------------------------------
        # close token, close connection
        # ---------------------------------------------
        self.connection_obj.send_finalize_connection()
        # ---------------------------------------------
        self.quit
        self.destroy()
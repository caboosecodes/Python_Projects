# Python Ver: 3.9.5
#
# Author :    Ricardo Lopez
#
# Purpose:    GUI for transferring files created within the last
#             24 hours
#
# Tested OS:  This code was written and tested to work with windows 10

from tkinter import *
from tkinter import filedialog
import tkinter as tk
from datetime import *
from datetime import datetime
import os
import shutil

# imports the other modules so we can have access to them
import transfer_gui
import transfer_func


# Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    #reference your class with self
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame configuration
        self.master = master
        self.master.minsize(500,300)
        self.master.title("Copy files within the last 24 hours")
        arg = self.master

        transfer_gui.load_gui(self)



if __name__ == "__main__":
    # creates the window from tkinter
    root = tk.Tk()
    # this is the class and pass through root
    App = ParentWindow(root)
    # keeps the window open
    root.mainloop()
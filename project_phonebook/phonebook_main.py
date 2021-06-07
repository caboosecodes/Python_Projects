# Python Ver:   3.9.5 
# 
# Author:       Ricardo Lopez
# 
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter, GUI module,
#               using Tkinter Parent and Child relationship.
# 
# Tested OS:    This code was writted and tested to work with windows 10.

from tkinter import *
from tkinter import messagebox
import tkinter as tk



# imports the other modules so we can have access to them
import phonebook_gui
import phonebook_func


# Frame is the Tkinter frame calss that our own class will inherit from
class ParentWindow(Frame):
    #reference your class with self
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width in pixels)
        self.master.maxsize(500,300)
        # references phonebook_func
        # this CenterWindow method will center our app on the user's screen
        # you have to pass in self to have access to all the widgets
        phonebook_func.center_window(self,500,300)
        # self.master is everything in the window
        self.master.title('The Tkinter Phonebook Demo')
        self.master.configure(bg='#F0F0F0')
        # This protocol method is a tkinter build-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        # "WM_DELETE_WINDOW" is microsoft windows syntax
        # if the X button is pressed then you call the lambda function which calls phonebook_func.askquit(self)) will close the window
        self.master.protocol('WM_DELETE_WINDOW', lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a serperate module
        # keeping your code comparmentalized and clutter free
        phonebook_gui.load_gui(self)

if __name__ == '__main__':
    # this creates the window from tkinter
    root = tk.Tk()
    # this is the class and passing through root
    App = ParentWindow(root)
    # keeps the window open
    root.mainloop()


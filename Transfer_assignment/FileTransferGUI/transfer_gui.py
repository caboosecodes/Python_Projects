from tkinter import *
from tkinter import filedialog
import tkinter as tk
from datetime import *
from datetime import datetime
import os
import shutil

import transfer_main
import transfer_func


def load_gui(self):

    # ***labels***
    # Label() is tkinter class for a label
    # you need to give it a class name, i.e. "self.lbl_source" when you instantiate Label()
    # grid() places it in the window
    self.lbl_source = tk.Label(self.master, text="Get files from...")
    self.lbl_source.grid(row = 0, column = 1, padx=(0,0), pady=(0,0))
    self.lbl_destination = tk.Label(self.master, text ="Send files to...")
    self.lbl_destination.grid(row = 2, column = 1, padx=(0,0), pady=(0,0))

    # ***buttons***
    # Button() is tkinter class for a button
    # class self.btn_source is the name for the Button() instantiation
    # grid() places it in the window
    self.btn_source =  tk.Button(self.master, width = 10, height = 1, text = "Browse", command = lambda: transfer_func.getSource(self))
    self.btn_source.grid(row = 1, column = 0, padx = (0,0), pady = (0,0))
    self.btn_destination = tk.Button(self.master, width = 10, height = 1, text = "Browse", command = lambda: transfer_func.getDestination(self))
    self.btn_destination.grid(row = 3, column = 0,  padx=(0,0), pady=(0,0))
    self.btn_copy = tk.Button(self.master, width = 10, height = 1, text = "Copy", command = lambda: transfer_func.copy(self))
    self.btn_copy.grid(row = 4, column = 1, padx=(0,0), pady=(0,0))

    # ***text***
    # Text() is tkinter class for a text field
    # class self.txt_source is the name for the Text() instantiation
    # grid() places it in the window
    self.txt_source = tk.Text(self.master, height = 1, font=("Arial", 12))
    self.txt_source.grid(row = 1, column = 1, padx = (0,0), pady = (0,0))
    self.txt_destination = tk.Text(self.master, height = 1, font=("Arial", 12))
    self.txt_destination.grid(row = 3, column = 1, padx = (0,0), pady = (0,0))







if __name__ == "__main__":
    pass

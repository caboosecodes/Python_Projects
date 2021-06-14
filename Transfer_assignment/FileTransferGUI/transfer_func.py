from tkinter import *
from tkinter import filedialog
import tkinter as tk
from datetime import *
from datetime import datetime
import os
import shutil

import transfer_main
import transfer_gui

def getSource(self):
    # filedialog.askdirectory() opens a window allowing you to select directory
    # sourcePath stores the string
    sourcePath = filedialog.askdirectory(initialdir="C:/", title="Select a folder")
    # insert it into text widget
    self.txt_source.insert(0, sourcePath)

def getDestination(self):
    # destinationPath stores the string
    destinationPath = filedialog.askdirectory(initialdir="C:/", title="Select a destination folder")
    # insert it into the text widget
    self.txt_destination.insert(0, destinationPath)

def copy(self):
    source = self.txt_source.get()
    destination = self.txt_destination.get()
    fileNames = os.listdir(source)

    for file in fileNames:
        # path for the file
        abPath = os.path.join(source, file)
        # gets time in a float
        modifySec = os.path.getmtime(abPath)
        # converts float in to datetime structure
        modifyTime = datetime.fromtimestamp(modifySec)
        
        # if the modyfied date is within the last day then copy over the file
        if modifyTime > (datetime.now() + timedelta(days=-1)):
            shutil.copy(abPath, destination)


if __name__ == "__main__":
    pass

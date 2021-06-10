
import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog

# Frame is the parent class in tkinter
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        
        # title of window
        self.master.title("Check files")

        
        # instantiate Button() from tkinter
        # when the browse button is pressed it will execute the getDirectory function
        self.btnBrowse = Button(self.master, text = "Browse...", width= 13, height = 1, command = lambda: getDirectory())
        self.btnBrowse2 = Button(self.master, text = "Browse...", width= 13, height = 1)
        self.btnCheck = Button(self.master, text = "Check for files...", width = 13, height = 2)
        self.btnClose = Button(self.master, text = "Close Program", width = 12, height = 2)

        # instantiate Entry() from tkinter
        self.txt = getPath()
        self.txt2 = Entry(self.master, text = "", width = 53)
        

        # grid places the button in the window
        self.btnBrowse.grid(row = 1, column = 0, padx = 15, pady = (40,0), sticky = S)
        self.btnBrowse2.grid(row = 2, column = 0, padx = 15, pady = 10, sticky = S)
        self.btnCheck.grid(row = 3, column = 0, padx = 15, pady=(0,20), sticky = S)
        self.btnClose.grid(row = 3, column = 3, padx = 15, pady=(0,20), sticky = SE)

        # place the entry window using grid()
        self.txt.grid(row = 1, column = 1, columnspan = 3, padx = 15, pady = (40,0))
        self.txt2.grid(row = 2, column = 1, columnspan = 3, padx = 15)


# function to open window asking for directory
def getDirectory():
    
    filePath = filedialog.askdirectory(initialdir="C:/", title="Select a path")
    
    return filePath





if __name__ == "__main__":
    root = Tk()

    app = ParentWindow(root)

    root.mainloop()

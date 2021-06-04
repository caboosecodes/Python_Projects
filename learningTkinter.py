

import tkinter
from tkinter import *


# frame is the parent class in tkinter
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        # unable to resize the window
        self.master.resizable(width=False, height=False)
        # 700 x 400 pixels
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg = 'lightgray')
        
        # Variable classes in tkinter
        # instantiate stringVar()
        self.varFName = StringVar()
        self.varLName = StringVar()
        # set() assigns it a value
        self.varFName.set('')
        self.varLName.set('')

        # comes up in console
        # get() gets the value that's been stored rather than object name
        print(self.varFName.get())
        print(self.varLName.get())

        #instantiate Label()
        self.lblFName = Label()

        self.lblFName = Label(self.master,text='First Name: ', font=('Helvetica', 16), fg = 'black', bg = 'lightgray' )
        # padx and pady is padding and the values entered are the number of pixels
        # if you want your item to take more than one column, you would write "colspan = " and however many columns
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))


        self.lblLName = Label(self.master,text='Last Name: ', font=('Helvetica', 16), fg = 'black', bg = 'lightgray' )        
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='', font=('Helvetica', 16), fg = 'black', bg = 'lightgray' )
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))
                              
        # calling a tkinter widget
        # place this entry on self.master
        self.txtFName = Entry(self.master,text=self.varFName, font=('Helvetica', 16), fg = 'black', bg = 'lightblue' )
        # pack() places it, and paints it onto the window
        # grid() needs parameters to know where to place it
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.txtLName = Entry(self.master,text=self.varLName, font=('Helvetica', 16), fg = 'black', bg = 'lightblue' )
        self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        #instantiate Button() and name it self.btnSubmit
        self.btnSubmit = Button(self.master, text = 'Submit', width=10, height=2, command=self.submit)
        # sticky tells it where to stick the button; N = north, E = east
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text = 'Cancel', width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)
        

    # self the class and submit is the method or function
    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        # when you want you change something dynamically use config()
        # inserts the 
        self.lblDisplay.config(text='Hello {} {}!'.format(fn, ln))

    def cancel(self):
        # destroy() closes the window
        self.master.destroy()
        



if __name__ == '__main__':
    # instantiated tkinter (Tk()) and named it root
    # the parent class comes from tkinter
    root = Tk()
    # attach root to ParentWindow
    # tkinter class is instantiated and ParentWindow() is instantiated
    App = ParentWindow(root)
    # most important line; w/o this function the window will not continously run
    root.mainloop()

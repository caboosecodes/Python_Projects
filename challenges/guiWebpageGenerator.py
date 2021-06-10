
from tkinter import *
from tkinter import font
from tkinter import Text
import webbrowser


# Frame is the parent class in tkinter
class Parentwindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        # sets the size of the window
        self.master.geometry("{}x{}".format(750, 700))
        self.master.title("Web Page Generator")


        # instantiate label for Text field
        self.labelHTML = Label(self.master, text="Write your text below:", font=("Arial", 16))
        # places the label in the window
        self.labelHTML.grid(row=0, column=0, padx=(5,0), pady=(25,0))

        # instantiates Text()
        self.codeText = Text(self.master, height=10, font=("Arial", 12))
        # places the Text() widget in the window
        self.codeText.grid(row=1, column=0, columnspan=2, padx=(15,15), pady=(5))
        # instantiates Button()
        self.btnGen = Button(self.master, text="Generate", width=15, height=2, command=self.generateWebpage)
        # places Button() widget in window
        self.btnGen.grid(row=2, column=1, padx=(0, 0), pady=(5,0), sticky=W)
        # instantiates Button()
        self.btnCan = Button(self.master, text="Cancel", width=15, height=2, command=self.cancel)
        # places Button() widget in window
        self.btnCan.grid(row=2, column=1, padx=(0, 15), pady=(5,0), sticky=E)
        
        
    # function to generate webpage
    def generateWebpage(self):
        # .get() retrives the content of Text() widget
        # set that content to textEntry variable
        textEntry = self.codeText.get("1.0", "end")
        # creates main.html or writes over it if it exists
        f = open("main.html", "w") 
        # writes in the document
        f.write("\
                <html>\
                    <body>\
                        <h1>\
                    {}\
                        </h1>\
                    </body>\
                </html>\
                ".format(textEntry))
        f.close()
        
        # opens main.html in a new tab in your web browser
        webbrowser.open_new_tab("main.html")

    # function cancel closes the window
    def cancel(self):
        self.master.destroy()




if __name__ == "__main__":
    #instantiated tkinter (Tk()) and name it root
    root = Tk()
    #tkinter class is instantiated and ParentWindow() is instantiated
    App = Parentwindow(root)
    #allows to continuously run
    root.mainloop()

        

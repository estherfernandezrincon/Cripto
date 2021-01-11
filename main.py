from tkinter import *
from tkinter import ttk

import cripto

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Cripto Inversiones")

        self.cripto = cripto.MainClass(self)
        self.cripto.pack(side=TOP)



if __name__=="__main__":
    app=MainApp()
    app.mainloop()
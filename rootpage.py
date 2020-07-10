import tkinter as tk
#import SLQfunc as sql

class Rootwindow:
    
    def __init__(self, rootname, password):
        self.__rootname = rootname    
        self.__password = password
        self.window = tk.Tk()
        self.w_window = self.window.winfo_screenwidth()
        self.h_window = self.window.winfo_screenheight()
        self.width = 800
        self.height = 600
        self.posx, self.posy = self.w_window/2 - self.width/2, self.h_window/2 - self.height/2
        
        self.window.title("Root")
        self.window.geometry("%dx%d+%d+%d" % (self.width, self.height, self.posx, self.posy))
        self.window.resizable(False, False)
        self.window.mainloop()

from tkinter import (Label, LabelFrame, Button, Tk, Menu, filedialog)


class Window:

    def __init__(self, windowname):
        self.windowname = windowname
        
        self.window = Tk()
        self.w_window = self.window.winfo_screenwidth()
        self.h_window = self.window.winfo_screenheight()
        self.width = 800
        self.height = 500
        self.window_configure()   
        self.mainmenu() 
        self.window.mainloop()
    
    def __str__(self):
        return "Window: {}".format(self.windowname)

    def window_configure(self):
        posx, posy = self.w_window/2 - self.width/2, self.h_window/2 - self.height/2        
        self.window.title(self.windowname)
        self.window.geometry("%dx%d+%d+%d" % (self.width, self.height, posx, posy))
        self.window.resizable(False, False)
    
    def _cascademenu(self, menu, labelname):
        newmenu = Menu(menu, tearoff=0)
        menu.add_cascade(menu=newmenu, label=labelname)
        return newmenu

    def mainmenu(self):
        main = Menu(self.window)
        menufile = self._cascademenu(main, "File")
        menufile.add_command(labe="Save File")
        
        menumode = self._cascademenu(main, "Mode")
        menumode.add_command(label="Graphic Mode")
        menumode.add_separator()
        menumode.add_command(label="Table Mode")


        self.window.config(menu=main)    

    

Window('root')
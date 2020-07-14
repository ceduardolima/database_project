
from tkinter import (Label, LabelFrame, Frame, Button, Tk, Menu, Entry, StringVar)

class RootWindow:
    def __init__(self, size=(800,500)):
        self.window = Tk()
        self.w_screen = self.window.winfo_screenwidth()
        self.h_screen = self.window.winfo_screenheight()
        self.x, self.y = size
        self.submenu = []
        
        self.size_and_geomtry_configure()
        self.menuBar()

        self.visualframe = self.visualframes()
        self.visualframe.place(x=0,y=0)
        
        self.var = self.entry()
       
        self.window.mainloop()


    def size_and_geomtry_configure(self):
        w_window, h_window = self.x, self.y
        pos_x, pos_y = self.w_screen/2 - w_window/2, self.h_screen/2 - h_window/2
        self.window.geometry("%dx%d+%d+%d" % (w_window, h_window, pos_x, pos_y))
        self.window.resizable(False, False)
    
    #Menu bar
    def menuBar(self):
        # define menu class
        mainmenu = Menu(self.window)
        for n in range(3):
            optionsmenu = Menu(mainmenu, tearoff=0) 
            self.submenu.append(optionsmenu)

        # creating cascade
        mainmenu.add_cascade(menu=self.submenu[0], label="File")
        mainmenu.add_cascade(menu=self.submenu[1], label="Mode")
        mainmenu.add_cascade(menu=self.submenu[2], label="Tables")

        # creating command button 
        self.submenu[0].add_command(label="Save")
        self.submenu[1].add_command(label="Graphic")
        self.submenu[1].add_command(label="Table")
        self.submenu[2].add_command(label="Peças")
        self.window.config(menu=mainmenu)
   
        # frames
    def visualframes(self):
        visualframe = Frame(
            self.window,
            width=self.x,
            height=self.y,
            bg="#282a36"
        )
        return visualframe
    
    # Entry frame
    def entry(self):
        var = StringVar()
        Entry(
            self.visualframe,
            textvariable=var,
            width=133
        ).place(x=0, y=self.y-self.y/25)
        return var
    # receive sql
    def show(self, result):
        Label(
            self.visualframe,
            text=result,
            font="Arial 20",
            justify="center",
            width=114,
            height=31,
            anchor="nw",
            bg="#282a36",
            fg="#50fa7b"
        ).place(x=0,y=0)

RootWindow()

import tkinter as tk
#import SLQfunc as sql

class Rootwindow:
    
    def __init__(self, rootname='', password=''):
        self.__rootname = rootname    
        self.__password = password

    def __str__(self):
        return "ADM window"

    def __repr__(self):
        return "Rootwindow('{}', '{}')".format(self.__rootname, self.__password)

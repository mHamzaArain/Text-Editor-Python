import tkinter as tk                                # tkinter

from settings import Settings               # Basic settings 
from menu import Menu                      # Menu 
from toolbar import Toolbar                 # Toolbar(font, fontSize, fontColor,alignment)
from text_write import TextWrite          # Text (i.e; where to write)
from statusbar import Statusbar           # Statusbar(for word count) 

# Tk -> It is mediator b/w OS and Pyhon to work on GUI.
root = tk.Tk()                 

settings = Settings(root)                                              # Basic settings 
toolbar = Toolbar(root, settings)                                 # Toolbar(font, fontSize, fontColor, alignment)
text_write = TextWrite(root, toolbar)                           # Text (i.e; where to write)
statusbar = Statusbar(root, text_write)                         # Statusbar(for word count)
menu = Menu(root, settings, text_write,                      # Menu
                     statusbar, toolbar) 

# mainloop -> Sustained our program not to close self assertive.
root.mainloop()
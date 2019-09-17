import tkinter as tk
from tkinter import ttk

class Statusbar:
    '''Display statusbar on bottom written 'Status Bar'
    by default  when change occur in text edit
    (i.e; char or word typed) then select each char/word
    { from start- [ end-1char (i.e; not to include white spaces) ] }
    & split it into words and chars to display on statusbar. '''
    
    def __init__(self, windows, text_write):
        self.root = windows
        self.text_write = text_write
        
        ##Status bar
        # 'Status Bar' text on label by default but text change later 
        # set statusbar on bottom
        self.status_bar = ttk.Label(self.root, text='Status Bar')               
        self.status_bar.pack(side=tk.BOTTOM)

        # text_changed -> To work with exit() in  menu.py  
        # nothing in text editor
        self.text_changed = False   
        
        # '<<Modified>>' -> any change(i,.e; text in text editor)
        self.text_write.text_editor.bind('<<Modified>>', self.changed)  
    
    ###Status bar
    def changed(self, event=None):
        # Change in text editor(i.e; empty to increase in characters)
        if self.text_write.text_editor.edit_modified():
            self.text_changed = True                                        # text editor has some text 
            self.text_write.text_editor.get(1.0, 'end-1c').split()  #(start - end-1char) > This delete last char
                            #  because of it count when line changes
            
            # count word through  split() -> for each word
            # count characters
            words = len(self.text_write.text_editor.get(1.0, 'end-1c').split())             
            characters = len(self.text_write.text_editor.get(1.0, 'end-1c'))                
            
            # Shows count of chars & words
            self.status_bar.config(text=f'Characters: {characters}  Words: {words}') 
       
        # to make our code false to work again
        self.text_write.text_editor.edit_modified(False)                                           



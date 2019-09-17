import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class Menu():
    def __init__(self,windows , ai_settings, text_write, status_bar, toolbar):
        # Inheritance
        self.root = windows                         # root
        self.ai_settings = ai_settings            # ai_settings
        self.text_write = text_write               # text_write
        self.statusbar = status_bar               # statusbar
        self.tool_bar_show = toolbar            # toolbar

        # Menu configuration
        self.menu = tk.Menu(self.root)
        self.root.configure(menu=self.menu)

        ####images for sub-menu
        ###file
        #Mian menu: file -> sub menu icons                                                                ## File
        self.new_icon = tk.PhotoImage(file=self.ai_settings.exact_path('new.png'))            # new 
        self.open_icon = tk.PhotoImage(file=self.ai_settings.exact_path('open.png'))         # open
        self.save_icon = tk.PhotoImage(file=self.ai_settings.exact_path('save.png'))            # save
        self.save_as_icon = tk.PhotoImage(file=self.ai_settings.exact_path('save_as.png'))  # save as
        self.exit_icon = tk.PhotoImage(file=self.ai_settings.exact_path('exit.png'))                # exit

        ###edit 
        #Mian menu: edit -> sub menu icons                                                              ## Edit
        self.copy_icon = tk.PhotoImage(file=self.ai_settings.exact_path('copy.png'))           # copy
        self.paste_icon = tk.PhotoImage(file=self.ai_settings.exact_path('paste.png'))         # paste
        self.cut_icon = tk.PhotoImage(file=self.ai_settings.exact_path('cut.png'))                 # cut
        self.clear_all_icon = tk.PhotoImage(file=self.ai_settings.exact_path('clear_all.png'))  # clear
        self.find_icon = tk.PhotoImage(file=self.ai_settings.exact_path('find.png'))               # find 

        ###view icons 
        #Mian menu: view icons -> sub menu icons                                                       ## View
        self.tool_bar_icon = tk.PhotoImage(file=self.ai_settings.exact_path('tool_bar.png'))       # toolbar
        self.status_bar_icon = tk.PhotoImage(file=self.ai_settings.exact_path('status_bar.png')) # statusbar

        ###color theme 
        #Mian menu: view icons -> sub menu icons                                                       ## View
        self.light_default_icon =  tk.PhotoImage(file=self.ai_settings.exact_path('light_default.png')) # light
        self.light_plus_icon = tk.PhotoImage(file=self.ai_settings.exact_path('light_plus.png'))           # light+
        self.dark_icon = tk.PhotoImage(file=self.ai_settings.exact_path('dark.png'))                            # dark
        self.red_icon = tk.PhotoImage(file=self.ai_settings.exact_path('red.png'))                                # red
        self.monokai_icon = tk.PhotoImage(file=self.ai_settings.exact_path('monokai.png'))              # monokai
        self.night_blue_icon = tk.PhotoImage(file=self.ai_settings.exact_path('night_blue.png'))        # night blue

        # Joining(relate & cascade) sub-menues to main menu
        self.file = tk.Menu(self.menu, tearoff=False)                   # file
        self.edit = tk.Menu(self.menu, tearoff=False)                  # edit
        self.view = tk.Menu(self.menu, tearoff=False)                 # view
        self.color_theme = tk.Menu(self.menu, tearoff=False)     # color theme

        self.menu.add_cascade(menu=self.file, label='File')                               # File
        self.menu.add_cascade(menu=self.edit, label='Edit')                             # Edit
        self.menu.add_cascade(menu=self.view, label='View')                           # View
        self.menu.add_cascade(menu=self.color_theme, label='Color Theme')  # Color Theme

        ##   File commands
        ## [].add_command(
        # label -> to show text,
        # image -> put image,
        # comppund -> take string left,
        # accelarator -> To show short cut on right side,
        # command -> to relate function)
        self.file.add_command(label='New', image=self.new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=self.new_file)
        self.file.add_command(label='Open', image=self.open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=self.open_file)
        self.file.add_command(label='Save', image=self.save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command=self.save_file)
        self.file.add_command(label='Save As', image=self.save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=self.save_as)
        self.file.add_command(label='Exit', image=self.exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=self.exit)

        ## Edit commands
        # .event_generate("<Control c>") ->  by key/select from menu
        self.edit.add_command(label='Copy', image=self.copy_icon, compound=tk.LEFT, accelerator='Ctrl+C', command=lambda : self.text_write.text_editor.event_generate("<Control c>"))
        self.edit.add_command(label='Paste', image=self.paste_icon, compound=tk.LEFT, accelerator='Ctrl+V', command=lambda : self.text_write.text_editor.event_generate("<Control v>"))
        self.edit.add_command(label='Cut', image=self.cut_icon, compound=tk.LEFT, accelerator='Ctrl+X', command=lambda : self.text_write.text_editor.event_generate("<Control x>"))
        self.edit.add_command(label='Clear All', image=self.clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X', command= lambda : self.text_write.text_editor.delete(1.0, tk.END))
        self.edit.add_command(label='Find', image=self.find_icon, compound=tk.LEFT, accelerator= 'Ctrl+F', command=self.find_replace)

        ###View
        #View check buttons
        self.show_toolbar = tk.BooleanVar()         
        self.show_toolbar.set(True)                     # Show toolbar
        self.show_statusbar = tk.BooleanVar()
        self.show_statusbar.set(True)                  # Show statusbar
        
        ## view Checkbutton
        self.view.add_checkbutton(label='Tool Bar',
            image=self.tool_bar_icon,       # put image
            compound=tk.LEFT,                # put text on left side
            onvalue=1, offvalue=0,           # put values T/F
            variable=self.show_toolbar,     # Responsible for switching T/F
            command=self.hide_toolbar)  # to relate function

        # Statusbar Checkbutton
        self.view.add_checkbutton(label='Status Bar',
            image=self.status_bar_icon,         # put image
            compound=tk.LEFT,                      # put text on left side
            onvalue=True, offvalue=False,      # put values T/F
            variable=self.show_statusbar,       # Responsible for switching T/F
            command=self.hide_statusbar)     # to relate function

        ###Theme Color
        # Put theme 
        self.theme_choice = tk.StringVar()    

        # theme choices -> images in tuple 
        self.color_icons = (self.light_default_icon, 
             self.light_plus_icon,
             self.dark_icon, 
             self.red_icon,
             self.monokai_icon, 
             self.night_blue_icon)

        # switching background 
        self.color_dict = {
            'Light Defalut' : ('#000000', '#ffffff'),
            'Light  Plus' : ('#474747', '#e0e0e0'),
            'Dark' : ('#c4c4c4', '#2d2d2d'),
            'Red' : ('#2d2d2d', '#ffe8e8'),
            'Monokai' : ('#d3b774', '#474747'),
            'Night Blue' : ('#ededed', '#6b9dc2')
        }

        # Color Themes Radio button
        for count, item in enumerate(self.color_dict):                          # E.g:
            self.color_theme.add_radiobutton(label= item, # 'Light Defalut'
              image= self.color_icons[count],                        # Put image from tuple ->light_default_icon
              variable= self.theme_choice,                             # Set (as StringVar())  only 1 at a time
              compound=tk.LEFT,                                           # Left text
              command=self.change_theme)                         # relate to function
        
    ###       functionalities for File
    # New File Function
    def new_file(self):
        '''Delete all char'''
        self.url = ''
        # Delete from start to end
        self.text_write.text_editor.delete(1.0, tk.END) 

    #Open File Function
    def open_file(self, event=None):
        #filedialog.askopenfilename -> working path, filetype= ( (Any file name,  txt file extension ), ( All files, Any ext ) )
        self.url = filedialog.askopenfilename(initialdir=os.getcwd(), title= 'Select File', filetype=(('Text File', '*.txt'), ('All files', '*.*')))  
        try:
            with open(self.url) as fr: #File read
                self.text_write.text_editor.delete(1.0, tk.END) # if there is already written in text editor it will delete all text
                self.text_write.text_editor.insert(1.0, fr.read()) #insert choosen file in text editor
        except FileNotFoundError:
            return
        except:
            return
      
    
    def save_file(self, event=None): 
        try:
            if self.url: # if text file is alredy open or saved previous version
                content = str(text_write.text_editor.get(1.0, tk.END))
                with open(self.url, 'w', encoding='utf-8') as fw: #file writer
                    fw.write(content)
            else:# if text file is alredy open or saved previous version
                    # filedialog.asksaveasfilename(file mode, default extension, file types to write)
                self.url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                content2 = self.text_write.text_editor.get(1.0, tk.END)
                self.url.write(content2)
                self.url.close()    
        except:
                return 

        # save as  Function
    def save_as(self, event=None):
        try:
            content = self.text_write.text_editor.get(1.0, tk.END)
            # filedialog.asksaveasfilename(file mode, default extension, file types to write)
            self.url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            self.url.write(content)
            self.url.close()
        except:
            return 
    def exit(self, event=None):
        try:
            if self.statusbar.text_changed: # text_changed = True -> text changed/modified
                mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file?') # Options -> Yes/No/Cancel
                    # no option forked for -> CANCEL, only for -> YES, NO
                    #if user select -> YES
                if mbox is True:   #we want to change the file
                    if self.url: # file exist in text editor
                        content = self.text_write.text_editor.get(1.0, tk.END) # get from biginning to last
                        with open(self.url, 'w', encoding='utf-8') as fw: #filewriter
                            fw.write(content)
                            self.root.destroy() # to cancel window
                    else: #file not exist in text editor
                        content2 = str(self.text_write.text_editor.get(1.0, tk.END))
                            #path to save file-> filedialog.asksaveasfilename(file mode, default extension, file types to write)
                        self.url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                        self.url.write(content2)
                        self.url.close()
                        self.root.destroy()
                    # If User select -> No  , text in  editor and we destroyed it
                elif mbox is False:
                    self.root.destroy()
                # If text_change = False -> deitor has no text
            else:
                self.root.destroy()
            # If user select  
        except:
            return 

    def find_replace(self):
        def find():
            word = find_input.get() # getting word from entrybox
            #.tag_remove() ->  removing tag (backforund, foreground)
            #arg( <default word to match>, 1st char of text editor, lastt char of text editor)
            self.text_write.text_editor.tag_remove('match', '1.0', tk.END) # in this module start position is 1;  this means that start from bigining & ends it till the last
            matches = 0
            if word:
                start_pos = '1.0' #single char len
                while True:
                    #to search a word-> arg(searching word, strt pos of text editor, end pos of text editor)
                    start_pos = self.text_write.text_editor.search(word, start_pos, stopindex=tk.END)
                    if not start_pos: # this reads till the & not  found word in text editor
                        break 
                    end_pos = f'{start_pos}+{len(word)}c' # c deosnt count spaces
                    self.text_write.text_editor.tag_add('match', start_pos, end_pos)
                    matches += 1
                    start_pos = end_pos
                    #after word found tag changed for spacific word
                    self.text_write.text_editor.tag_config('match', foreground='red', background='yellow')

        def replace():
            #same word from find func
            word = find_input.get()
            replace_text = replace_input.get() # we input in replace entry box
            content = self.text_write.text_editor.get(1.0, tk.END) # 1st - last char from text editor
            new_content = content.replace(word, replace_text)  # word to replace 
            self.text_write.text_editor.delete(1.0, tk.END) # delete old word
            self.text_write.text_editor.insert(1.0, new_content) # insert replaceable word

        find_dialogue = tk.Toplevel() # tk.Toplevel() -> window inside window
        find_dialogue.geometry('450x250+500+200') # window size
        find_dialogue.title('Find') # title
        find_dialogue.resizable(0,0) # Not to resize again

        ## frame 
        find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
        find_frame.pack(pady=20)

        ## labels
        text_find_label = ttk.Label(find_frame, text='Find : ')
        text_replace_label = ttk.Label(find_frame, text= 'Replace')

        ## entry 
        find_input = ttk.Entry(find_frame, width=30)
        replace_input = ttk.Entry(find_frame, width=30)

        ## button 
        find_button = ttk.Button(find_frame, text='Find', command=find)
        replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

        ## label grid 
        text_find_label.grid(row=0, column=0, padx=4, pady=4)
        text_replace_label.grid(row=1, column=0, padx=4, pady=4)

        ## entry grid 
        find_input.grid(row=0, column=1, padx=4, pady=4)
        replace_input.grid(row=1, column=1, padx=4, pady=4)

        ## button grid 
        find_button.grid(row=2, column=0, padx=8, pady=4)
        replace_button.grid(row=2, column=1, padx=8, pady=4)

        find_dialogue.mainloop()

    def hide_toolbar(self):
        if self.show_toolbar:  #if toolbar appears 
            self.tool_bar_show.tool_bar.pack_forget() # hide toolbar
            self.show_toolbar = False  #-> maunupulate to command as under 
        else :  #if toolbar not appear  -> Arrange everythong again cause of toolbar seems insanely
            self.text_write.text_editor.pack_forget()  # remove editor
            self.statusbar.status_bar.pack_forget() # remove statusbar
            self.tool_bar_show.tool_bar.pack(side=tk.TOP, fill=tk.X)  # alingning toolbar
            self.text_write.text_editor.pack(fill=tk.BOTH, expand=True) # aligning text editor
            self.statusbar.status_bar.pack(side=tk.BOTTOM)  #aligning statusbar
            self.show_toolbar = True #-> maunupulate to command as under          
    def hide_statusbar(self):
        if self.show_statusbar:  # if statusbar appears already
            self.statusbar.status_bar.pack_forget() # remove status bar
            self.show_statusbar = False #-> maunupulate to command as under 
        else :
            self.statusbar.status_bar.pack(side=tk.BOTTOM) # if statusbar doesnt  appear 
            self.show_statusbar = True #-> maunupulate to command as under 

    ## color theme functionality
    def change_theme(self):
        chosen_theme = self.theme_choice.get() # user select what theme directly goes inside
        # choose theme & get value ('#000000', '#ffffff') from  dict  e.g;  'Light Defalut' : ('#000000', '#ffffff')
        color_tuple = self.color_dict.get(chosen_theme)  
        fg_color, bg_color = color_tuple[0], color_tuple[1] #color_dict = {  theme : (foreground, background) }
        self.text_write.text_editor.config(background=bg_color, fg=fg_color) 
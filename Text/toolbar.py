import tkinter as tk
from tkinter import ttk, font

class Toolbar:
    '''Toolbar configuration:
    1. Combobox  -> Font Style, Font Size
    2. Buttons        -> Bold, Italic, Underline,
                                ColorChooserText,
                                Alignment (Left, Center, Right) '''
                                
    def __init__(self, windows, ai_sttings):
        self.root = windows
        self.ai_settings = ai_sttings

        ####Toolbar
        # Display toolbar on top in x axis
        self.tool_bar = ttk.Label(self.root)
        self.tool_bar.pack(side=tk.TOP, fill=tk.X)

        ###Combobox
        ##Font Combobox
        self.font_tuple = tk.font.families()        # All fonts
        self.font_family = tk.StringVar()           # Select font

        # width=23 -> width of Combobox
        #  textvariable=self.font_family -> set the value of font
        # state='readonly' -> only type not write
        self.font_box = ttk.Combobox(self.tool_bar, 
                      width=23,
                      textvariable=self.font_family,
                      state='readonly')  
        
        # Put all  fonts in Font box
        self.font_box['values'] = self.font_tuple    
       
       # Allignment & setting up font type = 'Ariel' 
        self.font_box.grid(row=0, column=0, padx=5)  
        self.font_box.current(11) 

        ##Size Box
        self.size_var = tk.IntVar()    # Select font size

        # width=5 -> width of Combobox
        #  textvariable=self.size_var -> set the value of font size
        # state='readonly' -> only type not write
        self.font_size = ttk.Combobox(self.tool_bar,
                     width=5,
                     textvariable = self.size_var,
                      state='readonly')

        # Putting font sizes in font size Combobox
        self.font_size['values'] = tuple(range(8, 80, 1))
        
        # Allignment & setting up font size = 11 
        self.font_size.grid(row=0, column=1, )
        self.font_size.current(5)

        ###Buttons -> Put an image & alignment of button
        ##Bold Button
        self.bold_icon = tk.PhotoImage(file=self.ai_settings.exact_path('bold.png'))
        self.bold_btn = ttk.Button(self.tool_bar, image=self.bold_icon)
        self.bold_btn.grid(row=0, column=3, padx=5)

        # Italic Button
        self.italic_icon = tk.PhotoImage(file=self.ai_settings.exact_path('italic.png'))
        self.italic_btn = ttk.Button(self.tool_bar, image=self.italic_icon)
        self.italic_btn.grid(row=0, column=4, padx=2)

        # Underline Button
        self.underline_icon = tk.PhotoImage(file=self.ai_settings.exact_path('underline.png'))
        self.underline_btn = ttk.Button(self.tool_bar, image=self.underline_icon, )
        self.underline_btn.grid(row=0, column=5, )

        # Font Colour Button
        self.font_color_icon = tk.PhotoImage(file= self.ai_settings.exact_path('font_color.png'))
        self.font_color_btn = ttk.Button(self.tool_bar, image=self.font_color_icon,)
        self.font_color_btn.grid(row=0, column=6, padx=2)

        # Align Left
        self.align_left_icon = tk.PhotoImage(file= self.ai_settings.exact_path('align_left.png'))
        self.align_left_btn = ttk.Button(self.tool_bar, image=self.align_left_icon, )
        self.align_left_btn.grid(row=0, column=7, padx=2)

        # Align Center
        self.align_center_icon = tk.PhotoImage(file= self.ai_settings.exact_path('align_center.png'))
        self.align_center_btn = ttk.Button(self.tool_bar, image=self.align_center_icon, )
        self.align_center_btn.grid(row=0, column=8, padx=2)

        # Align Right
        self.align_right_icon = tk.PhotoImage(file= self.ai_settings.exact_path('align_right.png'))
        self.align_right_btn = ttk.Button(self.tool_bar, image=self.align_right_icon, )
        self.align_right_btn.grid(row=0, column=9, padx=2)
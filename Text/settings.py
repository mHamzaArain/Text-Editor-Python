import os

class Settings:
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x500')
        self.root.title('Notepad')

        # icon
        try: self.root.wm_iconbitmap(self.exact_path('icon.ico'))
        except: pass  

    def exact_path(self, exact_file):
        # To find exact image of alien.
        # os.walk -> deeply browse each path, file & folder
        # os.getcd -> current working diecttory
        finalPath = ''
        for path, folder, file in os.walk(os.getcwd()):
            # Considering each path whose ends with img(i.e; img folder)
            if path.endswith('icons'):
                # join path e.g;  "C:\Users\Hamza Arain\Desktop\Alien Project v1.3\Ch12_Firing_fromShip\img" + "/"  + "ship.bmp"  
                finalPath = os.path.join(path, exact_file)
                break
        return finalPath
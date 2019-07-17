'''

File manager for `.terrabl` folder -- manages state mostly

'''
# --- Imports ---
# Local
from .folder import Folder

# Imported
import yaml
import os


# --- Main ---
class File_Manager:
    def __init__(self, location):
        # Bootstrap location abspath
        basepath = os.getcwd()

        combinedPath = basepath \
            + ("/" if location[0] is not "/" else "") + location \
            + ("/" if location[-1] is not "/" else "") + '.terrabl/'
        
        # Absolute path of base folder
        self.basepath = os.path.abspath(combinedPath) 

        # Make folder object for self
        self.createFolder(self.basepath, True)
        self.base = self.explore()

    
    def createFolder(self, folder, base=False):
        if not os.path.isdir(folder):
            os.mkdir(folder)
            if not base:
                self.base.addFolder(folder)
            return True
        else:
            if not base:
                self.explore()
            return False


    def explore(self):
        f = Folder(self.basepath, self)
        f.explore()
        return f
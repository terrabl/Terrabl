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
        self.basepath = os.getcwd()
        combinedPath = self.basepath \
            + ("/" if location[0] is not "/" else "") + location \
            + ("/" if location[-1] is not "/" else "") + '.terrabl/'
        self.base = os.path.abspath(combinedPath) # absolute path of base folder
        self.files = [] # all the files in .terrabl/
        self.folders = Folder(self.base, 'base') if createFolder(self.base) else self.explore(self.base) # folder struct of .terrabl/

    
    def createFolder(self, folder):
        if not os.path.isdir(folder):
            # TODO: Make folder
            return True
        else:
            return False
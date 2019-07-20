'''

File manager for `.terrabl` directory -- manages state mostly

'''
# --- Imports ---
# Local
from .dir import Dir

# Imported
import os


# --- Main ---
class TDir:
    def __init__(self, location):
        # Bootstrap location abspath
        basepath = os.getcwd()

        combinedPath = basepath \
            + ("/" if location[0] is not "/" else "") + location \
            + ("/" if location[-1] is not "/" else "") + '.terrabl/'
        
        # Absolute path of base folder
        self.basepath = os.path.abspath(combinedPath) 

        # Make folder object for self
        self.base = Dir(self.basepath)
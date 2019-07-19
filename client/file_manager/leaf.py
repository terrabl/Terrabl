'''

File Struct -- basically a tree leaf

'''
# --- Imports ---
# Local

# Imported
import os


# --- Main ---
class Leaf:
    def __init__(self, location, parent, abspath=True): # abspath (bool): if `location` is an absolute path
        # Set Parent
        self.parent=parent
        
        # Set identity
        if abspath: self.abspath = location.split('/')
        else: self.abspath = parent.abspath + location.split('/')
        self.name = self.abspath[-1] if self.abspath[-1] is not '' \
            else self.abspath[-2]

        # No Children


    def __repr__(self):
        return self.name
    
    
    def __str__(self):
        return str(self.name)

    def hasChild(self, location):
        ''' Checks for a child in self.children - does nothing because leaf

        Args:
            location (string): Relative path to child

        Returns:
            success (boolean): Whether the child exists
        '''
        return False

    
    def explore(self):
        ''' Recursive update - does nothing because leaf

        Args: None

        Returns:
            success (boolean): Whether the process was successful
        '''
        return True
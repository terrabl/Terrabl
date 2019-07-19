'''

Directory Struct -- basically a tree

'''
# --- Imports ---
# Local
from .leaf import Leaf

# Imported
import os


# --- Main ---
class Directory:
    def __init__(self, location, parent, abspath=True, explore=True):
        # Set Parent
        self.parent=parent
        
        # Set path
        if abspath: self.abspath = location.split('/')
        else: self.abspath = parent.abspath + location.split('/')
        self.path = '/'.join(self.abspath)

        self.name = self.abspath[-1] if self.abspath[-1] is not '' \
            else self.abspath[-2]

        # Start Children
        self.leaves = []
        self.dirs = []

        # Explore
        if explore: self.explore()


    def __repr__(self):
        return [{self.name: ([__repr__(node) for node in self.dirs], \
            [__repr__(node) for node in self.leaves])}]
    
    
    def __str__(self):
        return "{" \
            + f"{self.name}: ([{', '.join([str(node) for node in self.dirs])}],\
             [{','.join([str(node) for node in self.leaves])}])" + "}"

    def addLeaf(self, location):
        ''' Add a child file

        Args:
            location (string): Absolute path to child

        Returns:
            success (boolean): Whether the attempt was successful
        '''
        # TODO: add syntax
        return True

    
    def addDir(self, location):
        ''' Add a child directory

        Args:
            location (string): Absolute path to child

        Returns:
            success (boolean): Whether the attempt was successful
        '''
        # TODO: add syntax
        return True

    
    def removeLeaf(self, location):
        ''' Remove a child file

        Args:
            location (string): Absolute path to child

        Returns:
            success (boolean): Whether the attempt was successful
        '''
        # TODO: add syntax
        return True


    def removeDir(self, location):
        ''' Remove a child directory

        Args:
            location (string): Absolute path to child

        Returns:
            success (boolean): Whether the attempt was successful
        '''
        # TODO: add syntax
        return True


    def hasChild(self, location):
        ''' Checks for a child in self.children

        Args:
            location (string): Relative path to child

        Returns:
            success (boolean): Whether the child exists
        '''
        # TODO: add syntax
        return True

    
    def explore(self):
        ''' Recursive update

        Args: None

        Returns:
            success (boolean): Whether the operation was successful
        '''
        # Find all the immediate children
        children = next(os.walk())
        
        # Save all the children
        leaves = [Leaf(f"{self.path}/{l}", self) for l in children[2]]
        dirs = [Directory(f"{self.path}/{d}", self, True, False) \
            for d in children[1]]

        # Check if they were already accounted for
        leafNames = [l.name for l in self.leaves]
        leaves = list(filter(lambda l: l.name not in leafNames, self.leaves))
        dirNames = [d.name for d in self.dirs]
        dirs = list(filter(lambda d: d.name not in dirNames, self.dirs))

        # Explore Dirs
        map(lambda d: d.explore, dirs)
            
        # Add remaining children to list
        self.leaves += leaves
        self.dirs += dirs
        
        return True
'''

Directory Struct -- basically a tree

'''
# --- Imports ---
# Local
from .leaf import Leaf

# Imported
import yaml
import os


# --- Main ---
class Directory:
    def __init__(self, location, parent, abspath=True):
        # Set Parent
        self.parent=parent
        
        # Set identity
        if abspath: self.abspath = location.split('/')
        else: self.abspath = parent.abspath + location.split('/')
        self.name = self.abspath[-1] if self.abspath[-1] is not '' \
            else self.abspath[-2]

        # Start Children
        self.leaves = []
        self.dirs = []


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
            success (boolean): Whether the child exists
        '''
        successes = []

        # Find all the leaves
        for leaf in next(os.walk('/'.join(self.abspath)))[2]:
            successes.append(self.addLeaf(leaf))
        
        # Find all the directories
        for d in next(os.walk('/'.join(self.abspath)))[1]:
            successes.append(self.addDir(d))
            
        return False not in successes
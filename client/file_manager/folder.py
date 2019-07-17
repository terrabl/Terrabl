'''

Folder Struct -- basically a tree

'''
# --- Imports ---
# Local

# Imported
import yaml
import os


# --- Main ---
class Folder:
    def __init__(self, location, parent):
        # Set Parent
        self.parent=parent
        
        # Set identity
        self.abspath = location.split('/')
        self.name = self.abspath[-1] if self.abspath[-1] is not '' \
            else self.abspath[-2]

        # Start Children
        self.children = []


    def __repr__(self):
        return [{self.name: [__repr__(node) for node in children]}]
    
    
    def __str__(self):
        return "{" \
            + f"{self.name}: [{', '.join([str(node) for node in children])}]" \
            + "}"

    def addChild(self, location):
        ''' Add a child file

        Args:
            location (string): Absolute path to child

        Returns:
            success (boolean): Whether the attempt was successful
        '''
        # TODO: add syntax
        return True

    
    def addFolder(self, location):
        ''' Add a child folder

        Args:
            location (string): Absolute path to child

        Returns:
            success (boolean): Whether the attempt was successful
        '''
        # TODO: add syntax
        return True

    
    def removeChild(self, location):
        ''' Remove a child file

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
        # TODO: add syntax
        return True
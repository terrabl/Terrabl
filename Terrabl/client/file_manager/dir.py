'''

Dir Struct -- basically a tree

'''
# --- Imports ---
# Local
from .leaf import Leaf

# Imported
import os
import shutil


# --- Main ---
class Dir:
    def __init__(self, location, parent, explore=True):
        # Set Type
        self.type = "dir"
        
        # Set Parent
        self.parent=parent
        
        # Set path
        self.abspath = location.split('/')
        self.path = '/'.join(self.abspath)

        self.name = self.abspath[-1] if self.abspath[-1] is not '' \
            else self.abspath[-2]

        # Start Children
        self.leaves = []
        self.dirs = []

        # Explore
        if explore:
            self.explore()


    def __repr__(self):
        return [{self.name: ([__repr__(node) for node in self.dirs], \
            [__repr__(node) for node in self.leaves])}]
    
    
    def __str__(self):
        return "{" \
            + f"{self.name}: ([{', '.join([str(node) for node in self.dirs])}],\
             [{','.join([str(node) for node in self.leaves])}])" + "}"

    def addChild(self, location):
        ''' Add a child file

        Args:
            location (string): Absolute path to child

        Returns:
            (boolean): Whether the child exists
        '''
        c, i = self.isDirectChild(location)
        if c and (i is -1):
            if c is "dir":
                self.dirs.append(Dir(location, self))
            else:
                self.leaves.append(Leaf(location, self))
        elif i is not -1:
            return True
        else:
            d, i = self.findNearestAncestor(location)
            if not d:
                return False
            if i is -1:
                self.dirs.append(Dir(d))
            else:
                d.explore()
            return d.hasChild(location)
        return True


    def removeChild(self, location, yes=False, force=False):
        ''' Remove a child

        Args:
            location (string): Absolute path to child
            yes (boolean): Remove without warning, only for dirs
            force (boolean): Remove even if not accounted for (not in children)

        Returns:
            (boolean): Whether the location ever existed
        '''
        if self.hasChild(location):
            # If the location is a direct child
            l = self.findLeaf(location)
            if l:
                # Delete
                os.remove(location)
                self.leaves.remove(l)
            else:
                # If location is dir
                l = self.findDir(location)
                
                # Warning
                if not yes and len(l.leaves+l.dirs) is not 0: 
                    res = input('This is a directory and has children,'+
                                ' proceed? [Y/n]')
                    if res.lower() not in 'yes': 
                        return # kill
                
                # Delete
                shutil.rmtree(location)
                self.dirs.remove(l)
            return True
        elif (force): # not in children
            try:
                os.remove(location)
            except IsADirectoryError:
                shutil.rmtree(location)
            return False
        else: 
            return False


    def hasChild(self, location):
        ''' Checks for a child in self.children

        Args:
            location (string): Relative path to child

        Returns:
            (boolean): Whether the direct child exists
        '''
        if location in [l.path for l in self.leaves + self.dirs]:
            return True
        else:
            d, i = self.findNearestAncestor(location)
            if not d:
                return False
            if i is -1:
                d = Dir(d, self)
            else:
                d = self.dirs[i]
            return d.hasChild(location)

    
    def explore(self):
        ''' Recursive update

        Args: None

        Returns:
            success (boolean): Whether the operation was successful
        '''''' Recursive update

        Args: None

        Returns:
            success (boolean): Whether the operation was successful
        '''
        # Find all the immediate children
        children = next(os.walk())
        
        # Save all the children
        leaves = [Leaf(f"{self.path}/{l}", self) for l in children[2]]
        dirs = [Dir(f"{self.path}/{d}", self, False) \
            for d in children[1]]

        # Check if they were already accounted for
        leafNames = [l.name for l in self.leaves]
        leaves = list(filter(lambda l: l.name not in leafNames, self.leaves))
        dirNames = [d.name for d in self.dirs]
        dirs = list(filter(lambda d: d.name not in dirNames, self.dirs))

        # Explore Dirs
        map(lambda d: d.explore(), dirs)
            
        # Add remaining children to list
        self.leaves += leaves
        self.dirs += dirs
        
        return True
    
    def findNearestAncestor(self, location):
        ''' Get Ancestor

        Args: 
            location (string): absolute path of location

        Returns:
            ancestor (string): absolute path of ancestor
            i (integer): index of ancestor in self.dirs or -1 if not exists
        '''
        # Break up location
        split = location.split(self.path)
        
        # Check if this folder's path is even in the location's path
        if len(split) is 1:
            return False, -1
        
        # Split the remainder and get the nearest ancestor's abspath
        ancestor = f"{self.path}/{split[1].split('/')[0]}"
        
        # Check if in dirs
        try:
            i = [d.path for d in self.dirs].index(ancestor)
        except ValueError:
            i = -1
        
        # Return
        return ancestor, i
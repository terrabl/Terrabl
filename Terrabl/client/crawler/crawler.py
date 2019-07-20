'''

Project crawler for locating files

'''
# --- Imports ---
# Local

# Imported
import yaml
import os


# --- Main ---
class Crawler:
    def __init__(self, location):
        self.basepath = os.getcwd()
        combinedPath = self.basepath \
            + ("/" if location[0] is not "/" else "") + location \
            + ("/" if location[-1] is not "/" else "")
        self.location = os.path.abspath(combinedPath)
        
    
    def crawl(self, crawlString):
        ''' Get location of all files with name crawlString

        Args:
            crawlString (string): Filename (e.g.: 't.yaml') to locate


        Returns:
            locations (string[]): List of path strings of locations
        '''
        locations = []
        for root, dirs, files in os.walk(self.location):
            if crawlString in files: 
                locations.append(root + "/" + crawlString)

        return locations
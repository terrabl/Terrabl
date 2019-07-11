#!/usr/bin/env python3
'''

Terrabl CLI Main

Notes:

* This is intended to run using PYTHON3, please only write py3 compatible code 
    or your changes will not be accepted.
* Please be sure to obey the 80 character per line limit.
* Please be sure to comment your code using Sphinx commenting style
    https://pythonhosted.org/an_example_pypi_project/sphinx.html

Format:

Imports         -- packages used in this file
    Local       -- In py_lib directory
    Imported    -- If package not available as standard or via pip, download 
                    the source and add it to the py_lib directory

Helpers         -- Where all the code should be

Main            -- Main class and runner

'''

# --- Imports ---
# Local
from parser.parser import Parser

# Imported


# --- Helpers ---


# --- Main ---
class Terrabl:
    def __init__(self):
        # Get Arg Parser
        parser = Parser() # keep everything parser-related local
        
        # Add handlers
        parser.install.addHandler(self.installHandler)
        parser.init.addHandler(self.initHandler)
        parser.stage.addHandler(self.stageHandler)
        parser.apply.addHandler(self.applyHandler)

        # Get Args and Apply Function
        args = parser.parse_args()

        return args.func(args) # EOF

    def installHandler(self, args):
        return

    def initHandler(self, args):
        return

    def stageHandler(self, args):
        return

    def applyHandler(self, args):
        return

if __name__ == "__main__":
    Terrabl()
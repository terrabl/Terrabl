'''

Sub-parser for `install` command

'''
# --- Imports ---
# Local

# Imported
import yaml


# --- Main ---
class Parser:
    def __init__(self, parent):
        # Connect self to parent
        self.parent = parent
        self.parser = self.parent.subparsers.add_parser('install', \
            help="install help")

        with open("./installer/dependencies.yaml", 'r') as y:
            choices = yaml.safe_load(y).keys()

        # Add arguments
        self.parser.add_argument('installer', type=str, \
            help="Installer available this machine", choices=choices)

        self.parser.add_argument('-y', '--yes', action="store_true", \
            help="Skip confirmation")
        
        self.parser.add_argument('-s', '--silent', action="store_true", \
            help="Do not print anything")

    def addHandler(self, func):
        """ Setter for handler of subparser

        Args:
            func (function): function that takes args param from parser

        Returns:
            None
        """
        self.parser.set_defaults(func=func)
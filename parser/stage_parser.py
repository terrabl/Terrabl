'''

Sub-parser for `apply` command

'''
# --- Imports ---
# Local

# Imported


# --- Main ---
class Parser:
    def __init__(self, parent):
        # Connect self to parent
        self.parent = parent
        self.parser = self.parent.subparsers.add_parser('stage', \
            help="stage help")

        # Add arguments
        self.parser.add_argument('location', type=str, \
            help="Location of terrabl.yaml, default = \".\"", default=".")

    def addHandler(self, func):
        """ Setter for handler of subparser

        Args:
            func (function): function that takes args param from parser

        Returns:
            None
        """
        self.parser.set_defaults(func=func)
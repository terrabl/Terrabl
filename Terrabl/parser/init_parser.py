'''

Sub-parser for `init` command

'''
# --- Imports ---
# Local

# Imported


# --- Main ---
class Parser:
    def __init__(self, parent):
        # Connect self to parent
        self.parent = parent
        self.parser = self.parent.subparsers.add_parser('init', \
            help="init help")

        # Add arguments
        self.parser.add_argument('location', type=str, \
            help="Desired location of terrabl.yaml, default = \".\"", \
            default=".")
        
        self.parser.add_argument('-s', '--silent', action="store_true", \
            help="Do not use questionnaire (defaults only)")

    def addHandler(self, func):
        """ Setter for handler of subparser

        Args:
            func (function): function that takes args param from parser

        Returns:
            None
        """
        self.parser.set_defaults(func=func)
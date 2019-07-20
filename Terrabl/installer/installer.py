'''

Installer of non-python dependencies

'''
# --- Imports ---
# Local

# Imported
import yaml
import subprocess
import shlex
import time
import os


# --- Main ---
class Installer:
    def __init__(self, args):
        # Get dependencies
        current = os.path.dirname(__file__)
        with open(current+'/dependencies.yaml', 'r') as y:
            # type(self.ds) = dict
            self.ds = yaml.safe_load(y)

        # Set vars
        self.yes = args.yes
        self.installer = args.installer
        self.silent = args.silent

        
    def p(self, val):
        """ Print if self.yes

        Args:
            val (string): string to print

        Returns:
            None
        """
        if not self.silent: 
            print(val, flush=True)


    def exec(self, c):
        """ Blocking run command with error handling

        Args:
            c (string): String of UNIX command to run

        Returns:
            None
        """

        # Popen options
        options = { #                   Below is if silent was not chosen
            "stdout": subprocess.PIPE,
            "bufsize": 1,
            "universal_newlines": True
        }
        # } if not self.silent else { #   Below is if silent was chosen

        # }

        with subprocess.Popen(shlex.split(c), **options) as p:
            for line in p.stdout:
                self.p(line)
        
        if p.returncode != 0:
            raise subprocess.CalledProcessError(p.returncode, p.args)
            

    def install(self):
        """ Start install process

        Args:
            None

        Returns:
            None
        """
        # Start Timer
        t = time.time()

        # Handle user confirmation prompt
        toInstall = self.ds[self.installer].keys()
        warning = "This will install " + \
            ', '.join([e.capitalize() for e in toInstall]) +\
            ", is that alright? [Y/n]  " 
        if not self.yes and not (input(warning).lower() in "yes"):
            self.p("Process aborted gracefully by user.")
            return 

        self.p("Starting installer...")

        # Build subprocess queue
        queue = list(self.ds[self.installer].values())

        # Run subprocess queue and print stdout
        for command in queue:
            if type(command) is list:
                for c in command:
                    self.exec(c)
            else:
                self.exec(command)

        # Terminating 
        self.p("Completed process")


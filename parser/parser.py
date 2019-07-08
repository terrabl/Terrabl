# --- Imports ---
# Local
from .init_parser import Parser as initParser
from .stage_parser import Parser as stageParser
from .apply_parser import Parser as applyParser

# Imported
import argparse


# --- Main ---
class Parser:
    def __init__(self):
        # Argument parser
        self.parser = argparse.ArgumentParser(description="Terrabl Terraform Tool")

        # Subparsers
        self.subparsers = self.parser.add_subparsers(help="sub-command help")

        self.init = initParser(self)
        self.stage = stageParser(self)
        self.apply = applyParser(self)
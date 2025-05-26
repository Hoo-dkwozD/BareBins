#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Stub class modified by BinShell. 
This class should not be exposed directly but 
should only exist within BinShellManager's abstraction. 
It requires BinShellManager to modify its attributes and methods.
"""

# Python standard library imports
from argparse import Namespace
import cmd

# Local application/library imports
from barebins.shell.BinShell.BinShellAbsClass import BinShellAbsClass

class BinShell(cmd.Cmd, BinShellAbsClass):
    """
    A child class of cmd.Cmd that implements the shell.
    """

    name = ""
    args = None
    prompt = ""
    mod_prompt = ""
    intro = ""
    core = None

    def __init__(self, name: str, args: Namespace):
        """
        Initialize the child shell class.
        """
        super().__init__()
        self.name = name
        self.args = args

    def emptyline(self):
        pass

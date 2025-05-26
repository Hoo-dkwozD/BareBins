#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Stub class modified by BinShell. 
"""

# Python standard library imports
from argparse import Namespace
import cmd

# Local application/library imports
from barebins.shell.BinShell.BinShellAbsClass import BinShellAbsClass

class ChildShell(cmd.Cmd, BinShellAbsClass):
    """
    A child class of cmd.Cmd that implements the shell.
    """

    name = ""
    base_prompt = ""
    prompt = ""
    killchain = {}
    data_stage = {}

    def __init__(self, name: str, args: Namespace):
        """
        Initialize the child shell class.
        """
        super().__init__()
        self.name = name
        self.args = args

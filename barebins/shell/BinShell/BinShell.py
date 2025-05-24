#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Basic interactive shell for carrying out developed exploits.
"""

# Python standard library imports
from argparse import Namespace
import cmd
from typing import Any, Optional

# Third-party library imports

# Local application/library imports
from utils.styles import f, s

class BinShell():
    """
    A simple command line shell for carrying out developed exploits.
    """

    def __init__(self, name: str, args: Namespace):
        """
        Initialize a shell class for the exploit.
        """

        self.name = name
        self.prompt = f"{f.b}[*] {name} >{s.R}"
        self.intro = f"Welcome to the {name} shell. Type help or ? to list commands.\n"

        class ChildShell(cmd.Cmd):
            """
            A child class of cmd.Cmd that implements the shell.
            """

            def __init__(self, name: str, args: Namespace):
                """
                Initialize the child shell class.
                """
                super().__init__()
                self.name = name
                self.args = args

        ChildShell.prompt = self.prompt
        ChildShell.intro = self.intro

        self.child_shell = ChildShell

    # TO-DO
    def load_help(self):
        """
        Load the enhanced help command for the shell. 

        :override:
        :param self: The shell instance.
        """
        pass

    def load_module(self, command_name: str, function: callable, help_text: str = None):
        """
        Load the modules for the shell.
        """
        
        setattr(self.child_shell, f"do_{command_name}", function)
        if help_text is not None:
            setattr(self.child_shell, f"help_{command_name}", help_text)

    def load_modules(self, modules: list[(str, callable, Optional[str])]):
        """
        Load the modules for the shell.
        """
        
        for module in modules:
            if len(module) == 2:
                self.load_module(module[0], module[1])
            elif len(module) == 3:
                self.load_module(module[0], module[1], module[2])
            else:
                print(f"{f.r}[!] Invalid module format. Must be (name, function) or (name, function, help_text).{s.R}")
                continue
            print(f"{f.g}[+] Loaded module: {module[0]}{s.R}")
            print(f"{f.g}[+] Help: {module[2]}{s.R}" if len(module) == 3 else f"{f.g}[+] No help text provided.{s.R}")

    def load_flow(self, core: Any):
        """
        Load the business logic core for the shell.
        """
        
        self.child_shell.core = core

    def start(self):
        """
        Start the shell.
        """
        
        self.child_shell(self.name, self.args).cmdloop()

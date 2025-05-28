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
from enum import Enum
from typing import Dict, Optional

# Local application/library imports
from barebins.shellcore.BinCore import BinCoreAbsClass
from barebins.shell.BinShell.BinShellAbsClass import BinShellAbsClass
from barebins.utils.styles import f, s

class BasicShell(cmd.Cmd, BinShellAbsClass):
    """
    A child class of cmd.Cmd that implements the BinShellAbsClass Abstract Class.

    Shell commands relating to exploit modules have to be loaded into the shell
    by a manager class before it can be run. 
    """

    def __init__(self, name: str, args: Namespace):
        """
        Initialize the child shell class.

        :param name: The name of the shell.
        :param args: The exploit script's starter arguments.
        """

        super().__init__()
        self.name: str = name
        self.args: Namespace = args
        self.prompt: str = f"{f.b}[*] {name} >{s.R}"
        self.mod_prompt: str = self.prompt
        self.intro: str = f"{f.g}[+] Welcome to the {name} shell. Type help or ? to list commands.{s.R}\n"
        self.killchain: Dict[Enum, Dict[str, str]] = {}
        self.core: Optional[BinCoreAbsClass] = None

    def preloop(self) -> None:
        """
        Prepare the shell before starting the command loop.
        This method can be used to set up any necessary state or configurations.

        :return: None
        """
    
        print(f"{f.b}Starting {self.name} shell...{s.R}")

    def postloop(self) -> None:
        """
        Clean up after the command loop has finished.
        This method can be used to perform any necessary cleanup or finalization.

        :return: None
        """
    
        print(f"{f.b}[+] Exited {self.name} shell{s.R}")
        print(f"{f.g}[+++] Thank you for using the {self.name} shell.{s.R}")

    def emptyline(self) -> None:
        """
        Do nothing on empty input.

        :return: None
        """
    
        print()

    def do_help(self, arg: Optional[str] = None) -> None:
        """
        Display help information for commands.

        :param arg: The command to display help for. If None, display all commands.
        :return: None
        """
        if arg:
            command = arg.strip()
            try:
                help_func = getattr(self, f"help_{command}")
                help_func()
            except AttributeError:
                print(f"{f.r}[!] Command '{command}' does not exist.{s.R}")
        else:
            help_header = "Available commands (type 'help <command>'):"
            help_header_line = "=" * len(help_header)

            print(f"{f.b}{help_header}")
            print(f"{help_header_line}{s.R}")
            print()
            for category, commands in self.killchain.items():
                print(f"{f.g}{category.name}:{s.R}")
                for command, help_text in commands.items():
                    print(f"  {f.c}{command}{s.R} - {help_text}")
                print()
            print(f"{f.b}Type 'help <command>' for more information on a specific command.{s.R}")
            print(f"{f.b}Type 'exit' to exit the shell.{s.R}")
            print(f"{f.b}Type 'clear' to clear the screen.{s.R}")
            print()

    def do_exit(self) -> bool:
        """
        Exit the shell.

        :return: Exit status (True to exit, False to continue).
        """
    
        print(f"{f.b}[+] Exiting {self.name} shell... {s.R}")
        return True

    def check_core(self) -> bool:
        """
        Check if the core is set.

        :return: True if the core is set, False otherwise.
        """

        if self.core is None:
            print(f"{f.r}[!] Core not set. Please set the core before using the shell.{s.R}")
            return False
        return True

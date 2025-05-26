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
from enum import Enum
from typing import Any, Optional

# Third-party library imports

# Local application/library imports
from barebins.shell.BinShell.ChildShell import ChildShell
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
        self.base_prompt = f"{f.b}[*] {name} >{s.R}"
        self.prompt = self.base_prompt
        self.intro = f"Welcome to the {name} shell. Type help or ? to list commands.\n"

        ChildShell.base_prompt = self.base_prompt
        ChildShell.prompt = self.prompt
        ChildShell.intro = self.intro

        self.child_shell = ChildShell

    def _add_module_to_killchain(self, killchain_cat: Enum, command_name: str, help_text: Optional[str] = None):
        """
        Add a module to the killchain category.

        :param killchain_cat: The category of the killchain.
        :param command_name: The name of the command.
        :param help_text: The help text for the command.
        """
        
        if not hasattr(self.child_shell, "killchain"):
            self.child_shell.killchain = {}
        
        if killchain_cat not in self.child_shell.killchain:
            self.child_shell.killchain[killchain_cat] = {}

        self.child_shell.killchain[killchain_cat][command_name] = help_text or "No help text provided."

    def _load_help(self):
        """
        Load the enhanced help command for the shell. 

        :override:
        :param self: The shell instance.
        """
        
        def help_command():
            """
            Display the help text for the shell.
            """

            help_header = "Available commands (type 'help <command>'):"
            help_header_line = "=" * len(help_header)

            print(f"{f.b}{help_header}")
            print(f"{help_header_line}{s.R}")
            for category, commands in self.child_shell.killchain.items():
                print(f"{f.g}{category.name}:{s.R}")
                for command, help_text in commands.items():
                    print(f"  {f.c}{command}{s.R} - {help_text}")
                print()
            print(f"{f.b}Type 'help <command>' for more information on a specific command.{s.R}")
            print(f"{f.b}Type 'exit' to exit the shell.{s.R}")
            print(f"{f.b}Type 'clear' to clear the screen.{s.R}")
            print()

        self.child_shell.do_help = help_command

    def _load_exit(self):
        """
        Load the exit command for the shell.

        :override:
        :param self: The shell instance.
        """

        def exit_command():
            """
            Exit the shell.
            """
        
            return True

        self.child_shell.do_exit = exit_command
        self.child_shell.help_exit = lambda: print(f"{f.b}Exit the shell.{s.R}")

    def load_module(self, killchain_cat: Enum, command_name: str, function: callable, help_text: str = None):
        """
        Load the modules for the shell.
        """

        self._add_module_to_killchain(killchain_cat, command_name)
        setattr(self.child_shell, f"do_{command_name}", function)
        if help_text is not None:
            setattr(
                self.child_shell, 
                f"help_{command_name}", 
                lambda: print(f"{f.b}{killchain_cat.name} Type: {help_text}{s.R}")
            )

    def load_modules(self, modules: list[(str, callable, Optional[str])]):
        """
        Load the modules for the shell.
        """
        
        for module in modules:
            if len(module) == 3:
                self.load_module(module[0], module[1], module[2])
            elif len(module) == 4:
                self.load_module(module[0], module[1], module[2], module[3])
            else:
                print(
                    f"{f.r}[!] Invalid module format. Must be (category, name, function) or (category, name, function, help_text).{s.R}"
                )
                continue
            print(f"{f.g}[+] Loaded module: {module[0]}{s.R}")
            print(f"{f.g}[+] Help: {module[2]}{s.R}" if len(module) == 3 else f"{f.g}[+] No help text provided.{s.R}")

    def load_flow(self, core: Any):
        """
        Load the business logic core for the shell.
        """

        def exit_shell(stop: bool, line: str):
            """
            Exit the shell.
            """
        
            if line == "exit" and stop:
                print(f"{f.b}Exiting the shell...\n{s.R}")
                return True
            else:
                return False
        
        self.child_shell.core = core
        self._load_exit()
        self.child_shell.postcmd = exit_shell
        self.child_shell.postloop = lambda: print(f"{f.b}Thank you for using Bare-Bins.\n\n{s.R}")
        self._load_help()

    def start(self):
        """
        Start the shell.
        """
        
        self.child_shell(self.name, self.args).cmdloop()

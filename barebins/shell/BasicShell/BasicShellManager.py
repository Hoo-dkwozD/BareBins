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
from enum import StrEnum
from typing import Optional, Union

# Local application/library imports
from barebins.shell.BasicShell.BasicShell import BasicShell
from barebins.shellcore import BinCoreAbsClass
from barebins.utils.flow.BinFlow import BinGraphAbsClass
from barebins.utils.styles import f, s

# Local types
type Module = Union[tuple[StrEnum, str, callable], tuple[StrEnum, str, callable, str]]

class BasicShellManager():
    """
    A simple command line shell for carrying out developed exploits.
    """

    def __init__(self, name: str, args: Namespace):
        """
        Initialize a shell class manager for the exploit.
        """

        self.name = name
        self.args = args
        self.child_shell = BasicShell(name, args)

    def _add_module_to_killchain(
        self, 
        killchain_cat: StrEnum, 
        command_name: str, 
        help_text: Optional[str] = None
    ) -> None:
        """
        Add a module to the killchain category.

        :param killchain_cat: The category of the killchain.
        :param command_name: The name of the command.
        :param help_text: The help text for the command.
        :return: None
        """
        
        if killchain_cat not in self.child_shell.killchain:
            self.child_shell.killchain[killchain_cat] = {}
            setattr(
                self.child_shell, 
                f"do_{killchain_cat.name}", 
                lambda: print(f"{f.b}Collection of {killchain_cat.name} commands{s.R}")
            )
            setattr(
                self.child_shell, 
                f"help_{killchain_cat.name}", 
                lambda: print(f"{f.b}{killchain_cat.value}{s.R}")
            )

        self.child_shell.killchain[killchain_cat][command_name] = help_text or "No help text provided."

    def load_module(
        self, 
        killchain_cat: StrEnum, 
        command_name: str, 
        function: callable, 
        help_text: str = None
    ) -> None:
        """
        Load the modules for the shell.

        :param killchain_cat: The category of the killchain.
        :param command_name: The name of the command.
        :param function: The function to be executed when the command is called.
        :param help_text: The help text for the command.
        :return: None
        """

        self._add_module_to_killchain(killchain_cat, command_name, help_text)
        setattr(self.child_shell, f"do_{command_name}", function)
        if help_text is not None:
            setattr(
                self.child_shell, 
                f"help_{command_name}", 
                lambda: print(f"{f.b}{killchain_cat.name} Type: {help_text}{s.R}")
            )
        else:
            setattr(
                self.child_shell, 
                f"help_{command_name}", 
                lambda: print(f"{f.b}{killchain_cat.name} Type: No help text provided.{s.R}")
            )

    def load_modules(self, modules: list[Module]) -> None:
        """
        Load the modules for the shell.

        :param modules: A list of modules to be loaded, each defined as a tuple.
        :return: None
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
            print(f"{f.g}[+] Loaded module: {module[1]}{s.R}")
            print(f"{f.g}[+] Help: {module[3]}{s.R}" if len(module) == 4 else f"{f.g}[+] No help text provided.{s.R}")

    def load_core(self, core: BinCoreAbsClass) -> None:
        """
        Load the business logic core for the shell.

        :param core: The core class that provides the back-end logic for the shell.
        :return: None
        """
        
        self.child_shell.core = core

    def load_flow(self, flow: BinGraphAbsClass, overwrite: bool) -> None:
        """
        Load the automated flow for the shell.

        :return: None
        """

        self.child_shell.core.set_flow(flow)

    def start(self) -> None:
        """
        Start the shell.

        :return: None
        """

        self.child_shell.cmdloop()

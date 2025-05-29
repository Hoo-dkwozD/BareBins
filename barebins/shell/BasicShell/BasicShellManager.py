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
from barebins.module.BinModule import BinModuleAbsClass
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

    def _add_module_to_killchain(self, module: BinModuleAbsClass) -> None:
        """
        Add a module to the killchain category.

        :param killchain_cat: The category of the killchain.
        :param command_name: The name of the command.
        :param help_text: The help text for the command.
        :return: None
        """
        
        if module.killchain_cat not in self.child_shell.killchain:
            self.child_shell.killchain[module.killchain_cat] = {}
            setattr(
                self.child_shell, 
                f"do_{module.killchain_cat.name}", 
                lambda: print(f"{f.b}Collection of {module.killchain_cat.name} commands{s.R}")
            )
            setattr(
                self.child_shell, 
                f"help_{module.killchain_cat.name}", 
                lambda: print(f"{f.b}{module.killchain_cat.value}{s.R}")
            )

        self.child_shell.killchain[module.killchain_cat][module.name] = module.help_text

    def load_module(self, module: BinModuleAbsClass) -> None:
        """
        Load the modules for the shell.

        :param killchain_cat: The category of the killchain.
        :param command_name: The name of the command.
        :param function: The function to be executed when the command is called.
        :param help_text: The help text for the command.
        :return: None
        """

        self._add_module_to_killchain(module)
        setattr(self.child_shell, f"do_{module.name}", function)
        setattr(
            self.child_shell, 
            f"help_{module.name}", 
            lambda: print(f"{f.b}{module.killchain_cat.name} Type: {module.help_text}{s.R}")
        )

    def load_modules(self, modules: list[BinModuleAbsClass]) -> None:
        """
        Load the modules for the shell.

        :param modules: A list of modules to be loaded, each defined as a tuple.
        :return: None
        """
        
        for module in modules:
            self.load_module(module)
            print(f"{f.g}[+] Loaded module: {module.name}{s.R}")
            print(f"{f.g}[+] Help: {module.help_text}{s.R}")

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

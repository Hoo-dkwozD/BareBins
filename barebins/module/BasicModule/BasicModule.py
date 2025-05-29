#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

The default basic module object containing an exploit function.
"""

# Local application/library imports
from enum import StrEnum
from barebins.module.BinModule import BinModuleAbsClass
from barebins.shell.BinShell import BinShellAbsClass

class BasicModule(BinModuleAbsClass):
    """
    Default basic module object containing an exploit function.
    """

    def __init__(
        self, 
        killchain_cat: StrEnum,
        name: str, 
        function: callable[[BinShellAbsClass, str], None],
        help_text: str = "No help text provided."
    ):
        """
        :param killchain_cat: The category of the module in the kill chain.
        :param name: The name of the module.
        :param function: The exploit function to be executed.
        :param help_text: Help text for the module, defaults to "No help text provided."

        Initialize a basic module object with the given name and function.
        """

        self.killchain_cat = killchain_cat
        self.name = name
        self.function = function
        self.help_text = help_text
#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Abstract class of a module objects containing exploit functions.
"""

# Python standard library imports
from abc import ABC, abstractmethod
from enum import StrEnum

# Local application/library imports
from barebins.shell.BinShell import BinShellAbsClass

class BinModuleAbsClass(ABC):
    """
    Abstract base class for a module object containing an exploit function.
    """

    # Attributes
    killchain_cat: StrEnum
    name: str
    function: callable[[BinShellAbsClass, str], None]
    help_text: str


    # Methods
    @abstractmethod
    def __init__(
        self, 
        killchain_cat: StrEnum,
        name: str, 
        function: callable[[BinShellAbsClass, str], None],
        help_text: str
    ):
        """
        :param killchain_cat: The category of the module in the kill chain.
        :param name: The name of the module.
        :param function: The exploit function to be executed.
        :param help_text: Help text for the module.

        Initialize a module object with the given name.
        """

        pass

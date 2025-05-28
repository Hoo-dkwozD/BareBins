#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Abstract class of the interactive shell for carrying out developed exploits.
"""

# Python standard library imports
from abc import ABC, abstractmethod
from argparse import Namespace
from typing import Optional

# Local application/library imports
from barebins.shellcore import BinCoreAbsClass

class BinShellAbsClass(ABC):
    """
    Abstract base class for a simple command line shell for carrying out developed exploits.
    """

    # Attributes
    name: str
    args: Namespace
    prompt: str
    mod_prompt: str
    intro: str
    core: BinCoreAbsClass

    # Methods
    @abstractmethod
    def __init__(self, name: str, args: Namespace):
        """
        Initialize a shell class for the exploit.
        """

        pass

    @abstractmethod
    def preloop(self) -> None:
        """
        Prepare the shell before starting the command loop.
        This method can be used to set up any necessary state or configurations.

        :return: None
        """

        pass

    @abstractmethod
    def postloop(self) -> None:
        """
        Clean up after the command loop has finished.
        This method can be used to perform any necessary cleanup or finalization.

        :return: None
        """

        pass

    @abstractmethod
    def cmdloop(self, intro: str = None) -> None:
        """
        Start the command loop for the shell.

        :param intro: Optional introduction message to display before the command loop starts.
        :return: None
        """

        pass

    @abstractmethod
    def emptyline(self) -> None:
        """
        Handle empty lines in the command loop.

        :return: None
        """

        pass

    @abstractmethod
    def do_help(self, arg: Optional[str]) -> None:
        """
        Display help information for the shell commands.
        
        :param arg: The command for which help is requested.
        :return: None
        """

        pass

    @abstractmethod
    def check_core(self) -> bool:
        """
        Check if the core is set.
        
        :return: True if the core is set, False otherwise.
        """

        pass

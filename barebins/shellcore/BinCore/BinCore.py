#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Basic shell core for carrying out developed exploits.
"""

# Python standard library imports
from enum import Enum
from typing import Any

# Local application/library imports
from barebins.shellcore.BinCore import BinCoreAbsClass
from utils.styles import f, s

class BinCore(BinCoreAbsClass):
    """
    A basic shell core class that serves as the core of the shell system.
    This class provides the back-end logic for the shells.
    """

    def __init__(self):
        """
        Initialize the core class for the shell.
        """

        self.data_stage = {}

    def set_flow(self, flow: Any) -> None:
        """
        Set the flow for the core class.

        :param flow: The flow to be set for the core class.
        """

        pass

    def autorun(self) -> None:
        """
        Automatically run the core class.
        This method can be implemented to handle automatic execution.
        """

        pass

    def update(self, category: Enum, command: str, data: Any) -> None:
        """
        Update the core class with new data.

        :param category: The killchain category of the command.
        :param command: The command the data is associated with.
        :param data: The new data.
        """

        if category not in self.data_stage:
            self.data_stage[category] = {}
        self.data_stage[category][command] = data

        print(f"{f.g}Updated {category} with command '{command}' and data: {data}{s.R}")

    def reset(self) -> None:
        """
        Reset the core class to its initial state.
        """

        self.data_stage.clear()
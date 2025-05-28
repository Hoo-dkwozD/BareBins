#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Basic shell core for carrying out developed exploits.
"""

# Python standard library imports
from typing import Any

# Local application/library imports
from barebins.shellcore.BinCore import BinCoreAbsClass
from barebins.utils.flow.BinFlow.BinGraph import BinGraphAbsClass
from utils.styles import f, s

# Local types
type DataStage = dict[str, Any]

class BasicCore(BinCoreAbsClass):
    """
    A basic shell core class that serves as the core of the shell system.
    This class provides the back-end logic for the shells.
    """

    def __init__(self):
        """
        Initialize the core class for the shell.
        """

        self.data_stage: DataStage = {}

    def set_flow(self, flow: BinGraphAbsClass) -> None:
        """
        Set the automated flow for the core class.

        :param flow: The graph defining the flow.
        :return: None
        """

        pass

    def autorun(self) -> None:
        """
        Automatically run the core class.

        :return: None
        """

        pass

    def update(self, command: str, data: Any) -> None:
        """
        Update the core class with new data.

        :param category: The killchain category of the command.
        :param command: The command the data is from.
        :param data: The new data after module execution.
        :return: None
        """

        self.data_stage[command] = data

        print(f"{f.g}Updated data under {command}: {data}{s.R}")

    def reset(self) -> None:
        """
        Reset the core class to its initial state.

        :return: None
        """

        self.data_stage.clear()

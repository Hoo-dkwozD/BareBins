#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Basic shell core for carrying out developed exploits.
"""

# Python standard library imports
from typing import Any, Optional

# Local application/library imports
from barebins.shell import BasicShell
from barebins.shellcore.BinCore import BinCoreAbsClass
from barebins.utils.flow.BasicFlow import BasicGraph
from barebins.utils.styles import f, s

# Local types
type DataStage = dict[str, Any]

class BasicCore(BinCoreAbsClass):
    """
    A basic shell core class that serves as the core of the shell system.
    This class provides the back-end logic for the shells.
    """

    _flow: Optional[BasicGraph] = None

    def __init__(self):
        """
        Initialize the core class for the shell.
        """

        self.data_stage: DataStage = {}

    @property
    def flow(self) -> BasicGraph:
        """
        :return: The graph defining the flow.

        Get the automated flow for the core class.
        """

        return self._flow

    @flow.setter
    def flow(self, flow: BasicGraph) -> None:
        """
        :param flow: The graph defining the flow.
        :return: None

        Set the automated flow for the core class.
        """

        self._flow = flow

    def has_flow(self) -> bool:
        """
        :return: Boolean indicating the presence of a flow object.

        Indicates whether a flow object has been set. 
        """

        return type(self._flow) == BasicGraph

    def init_flow(self, shell: BasicShell) -> None:
        """
        :param shell: The shell to which to add exploit modules to.
        :return: None

        Initialises the function modules from the flow object. 
        """

        pass

    def update(self, command: str, data: Any) -> None:
        """
        :param command: The command the data is from.
        :param data: The new data after module execution.
        :return: None

        Update the core class with new data.
        """

        self.data_stage[command] = data

        print(f"{f.g}[+] Updated data under {command}: {data}{s.R}")

    def reset(self) -> None:
        """
        :return: None

        Reset the core class to its initial state.
        """

        self.data_stage.clear()

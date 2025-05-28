#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Abstract class of the basic shell core for carrying out developed exploits.
"""

# Python standard library imports
from abc import ABC, abstractmethod
from enum import StrEnum
from typing import Any

# Local application/library imports
from barebins.utils.flow.BinFlow.BinGraph import BinGraphAbsClass

class BinCoreAbsClass(ABC):
    """
    Abstract base class for the core of the shell system.
    This class defines the interface for the shell core.
    """

    @abstractmethod
    def __init__(self):
        """
        Initialize the core class for the exploit shell.
        """

        pass

    @abstractmethod
    def set_flow(self, flow: BinGraphAbsClass) -> None:
        """
        Set the flow for the core class.

        :param flow: The flow to be set for the core class.
        :return: None
        """

        pass

    @abstractmethod
    def autorun(self) -> None:
        """
        Automatically run the exploit modules based on defined flow.

        :return: None
        """

        pass

    @abstractmethod
    def update(self, command: str, data: Any) -> None:
        """
        Update the core class with new data.

        :param category: The killchain category of the command.
        :param command: The command the data is associated with.
        :param data: The new data.
        :return: None
        """

        pass

    @abstractmethod
    def reset(self) -> None:
        """
        Reset the core class to its initial state.

        :return: None
        """

        pass
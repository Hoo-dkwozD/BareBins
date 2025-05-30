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
from barebins.shell.BinShell import BinShellAbsClass
from barebins.utils.flow.BinFlow.BinGraph import BinGraphAbsClass

class BinCoreAbsClass(ABC):
    """
    Abstract base class for the core of the shell system.
    This class defines the interface for the shell core.
    """

    _flow: BinGraphAbsClass

    @abstractmethod
    def __init__(self):
        """
        Initialize the core class for the exploit shell.
        """

        pass

    @property
    @abstractmethod
    def flow(self) -> BinGraphAbsClass:
        """
        :return: Graph representing module flow

        Return the flow of the core class.
        """

        pass

    @flow.setter
    @abstractmethod
    def flow(self, flow: BinGraphAbsClass) -> None:
        """
        :param flow: The flow to be set for the core class.
        :return: None

        Set the flow for the core class.
        """

        pass

    @abstractmethod
    def has_flow(self) -> bool:
        """
        :return: Boolean indicating presence of module flow object. 

        Indicates whether module flow object is properly set. 
        """

        pass

    @abstractmethod
    def setup_flow(self, shell: BinShellAbsClass) -> None:
        """
        :param shell: The shell to which to add exploit modules to.
        :return: None

        Initialises the function modules from the flow object. 
        """

        pass

    @abstractmethod
    def update(self, command: str, data: Any) -> None:
        """
        :param command: The command the data is associated with.
        :param data: The new data.
        :return: None

        Update the core class with new data.
        """

        pass

    @abstractmethod
    def reset(self) -> None:
        """
        :return: None

        Reset the core class to its initial state.
        """

        pass
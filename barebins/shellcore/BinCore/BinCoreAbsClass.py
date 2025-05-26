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
from enum import Enum
from typing import Any, Dict

class BinCoreAbsClass(ABC):
    """
    Abstract base class for the core of the shell system.
    This class defines the interface for the shell core.
    """

    @abstractmethod
    def __init__(self):
        """
        Initialize the core class for the shell.
        """

        pass

    @abstractmethod
    def set_flow(self, flow: Any) -> None:
        """
        Set the flow for the core class.
        This method should be implemented by subclasses to handle flow setting.

        :param flow: The flow to be set for the core class.
        """

        pass

    @abstractmethod
    def autorun(self) -> None:
        """
        Automatically run the core class.
        This method should be implemented by subclasses to handle automatic execution.
        """

        pass

    @abstractmethod
    def update(self, category: Enum, command: str, data: Any) -> None:
        """
        Update the core class with new data.
        This method should be implemented by subclasses to handle updates.

        :param category: The killchain category of the command.
        :param command: The command the data is associated with.
        :param data: The new data.
        """

        pass

    @abstractmethod
    def reset(self) -> None:
        """
        Reset the core class to its initial state.
        This method should be implemented by subclasses to handle resets.
        """

        pass
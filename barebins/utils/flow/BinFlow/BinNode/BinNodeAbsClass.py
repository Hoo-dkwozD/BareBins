#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Abstract class for defining a node in the BareBins flow graph.
"""

# Python standard library imports
from abc import ABC, abstractmethod
from enum import StrEnum
from typing import Any, Callable, Optional, Self

from barebins.shell.BinShell import BinShellAbsClass

# Local types
type EdgeLogic = Callable[[int, dict[str, Any]], Self]

class BinNodeAbsClass(ABC):
    """
    Abstract class for defining a node in the BareBins flow graph.
    """

    @abstractmethod
    def __init__(
        self, 
        killchain_cat: StrEnum, 
        name: str, 
        function: Callable[[BinShellAbsClass, str], None], 
        help_text: str
    ):
        """
        :param killchain_cat: The category of the node's exploit in the kill chain.
        :param name: The name of the node's exploit.
        :param function: The exploit function to be executed.
        :param help_text: Help text for the node's exploit.

        Initialize the node with details of its exploit.
        """

        pass

    @property
    @abstractmethod
    def edge_logic(self) -> EdgeLogic:
        """
        Set the next node(s) to go to after executing this node.

        :return: The function that dictates which node to go 
            to next based on inputs of `status` and `data`. 
        """

        pass

    @edge_logic.setter
    @abstractmethod
    def edge_logic(self, edge_logic: EdgeLogic) -> None:
        """
        Set the next node(s) to go to after executing this node.

        :param edge_logic: The function dictating which node to call next. 
            Accepts 2 arguments: `status` and `data`.
            Returns a Node.
        :return: None
        """

        pass

    @abstractmethod
    def goto(self, status: int, data: dict[str, Any]) -> Optional[Self]:
        """
        Returns the next node after executing this node.

        :return: Next Node
        """

        pass

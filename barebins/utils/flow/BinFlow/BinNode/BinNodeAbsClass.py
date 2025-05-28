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
from typing import Any, Callable, Dict

# Local types
type EdgeLogic = Callable[[int, Dict[str, Any]], None]

class BinNodeAbsClass(ABC):
    """
    Abstract class for defining a node in the BareBins flow graph.
    """

    @abstractmethod
    def __init__(self, name: str):
        """
        Initialize the node with a name.

        :param name: Name of the node.
        """

        self.name = name

    @abstractmethod
    def execute(self) -> None:
        """
        Execute the node's logic. 

        :return: None
        """

        pass

    @abstractmethod
    def goto(self) -> None:
        """
        Goes to the next node after executing this node.

        :return: None
        """

        pass

    @abstractmethod
    def set_goto(self, edge_logic: EdgeLogic) -> None:
        """
        Set the next node(s) to go to after executing this node.

        :param edge_logic: The function dictating which node to call next. 
            Accepts 2 arguments: `status` and `data`.
        :return: None
        """

        pass
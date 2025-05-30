#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Abstract class for defining a BareBins flow graph.
"""

# Python standard library imports
from abc import ABC, abstractmethod
from typing import Any, Optional

# Local application/library imports
from barebins.utils.flow.BinFlow.BinNode import BinNodeAbsClass

class BinGraphAbsClass(ABC):
    """
    Abstract class for defining the structure of a graph in BareBins.
    """

    @abstractmethod
    def __init__(self, name: str):
        """
        Initialize the graph structure.
        """

        pass

    @property
    @abstractmethod
    def start_node(self) -> Optional[BinNodeAbsClass]:
        """
        Return the starting node to the graph.

        :return: Starting node to the graph or None if not set.
        """

        pass

    @start_node.setter
    @abstractmethod
    def start_node(self, node: BinNodeAbsClass) -> None:
        """
        Add the starting node to the graph.

        :param node: The node to be added.
        :return: None
        """

        pass

    @property
    @abstractmethod
    def current_node(self) -> Optional[BinNodeAbsClass]:
        """
        Return the current node of the graph.

        :return: Current node to the graph or None if not set.
        """

        pass

    @current_node.setter
    @abstractmethod
    def current_node(self, node: BinNodeAbsClass) -> None:
        """
        Point to desired current node to the graph.

        :param node: The node to be set to.
        :return: None
        """

        pass

    @abstractmethod
    def next(self, status: int, data: dict[str, Any]) -> BinNodeAbsClass:
        """
        Execute the nodes of the graph based on their linked flow.

        :return: None
        """

        pass

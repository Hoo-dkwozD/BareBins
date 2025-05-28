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

# Local application/library imports
from barebins.utils.flow.BinFlow.BinNode import BinNodeAbsClass

class BinGraphAbsClass(ABC):
    """
    Abstract class for defining the structure of a graph in BareBins.
    """

    @abstractmethod
    def __init__(self):
        """
        Initialize the graph structure.
        """

        pass

    @abstractmethod
    def add_start_node(self, node: BinNodeAbsClass) -> None:
        """
        Add the starting node to the graph.

        :param node: The node to be added.
        :return: None
        """

        pass

    @abstractmethod
    def execute(self) -> None:
        """
        Execute the nodes of the graph based on their linked flow.

        :return: None
        """

        pass

#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Basic graph to represent a flow object. 
"""

# Python standard library imports
from typing import Any, Optional

# Local application/library imports
from barebins.utils.flow.BasicFlow.BasicNode import BasicNode
from barebins.utils.flow.BinFlow.BinGraph import BinGraphAbsClass


class BasicGraph(BinGraphAbsClass):
    """
    Abstract class for defining the structure of a graph in BareBins.
    """

    def __init__(self, name: str):
        """
        :param name: Name of the flow object. 

        Initialize the graph structure.
        """

        self.name = name

        self._start_node: Optional[BasicNode] = None
        self._current_node: Optional[BasicNode] = None

    @property
    def start_node(self) -> Optional[BasicNode]:
        """
        :return: Starting node to the graph.

        Return the starting node to the graph.
        """

        return self._start_node

    @start_node.setter
    def start_node(self, node: BasicNode) -> None:
        """
        :param node: The node to be added.
        :return: None

        Add the starting node to the graph.
        """

        self._start_node = node
        self._current_node = node

    @property
    def current_node(self) -> Optional[BasicNode]:
        """
        :return: Current node to the graph or None if not set.

        Return the current node of the graph.
        """

        return self._current_node

    @current_node.setter
    def current_node(self, node: BasicNode) -> None:
        """
        :param node: The node to be set to.
        :return: None

        Point to desired current node to the graph.
        """

        self._current_node = node

    def next(self, status: int, data: dict[str, Any]) -> BasicNode:
        """
        :param status: Status code of the execution of the current node.
        :param data: Data produced by the execution of the current node. 
        :return: Next node

        Produces the next node after execution of the current node.
        """

        if self._current_node is None:
            return None

        self._current_node = self._current_node.edge_logic(status, data)
        return self._current_node

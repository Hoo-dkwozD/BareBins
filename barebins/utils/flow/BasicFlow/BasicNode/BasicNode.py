#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Basic graph node to represent modules in a flow object. 
"""

# Python standard library imports
from enum import StrEnum
from typing import Any, Callable, Optional, Self

# Local application/library imports
from barebins.shell.BinShell import BinShellAbsClass
from barebins.utils.flow.BinFlow.BinNode import BinNodeAbsClass, EdgeLogic


class BasicNode(BinNodeAbsClass):
    """
    Implementation of basic node representing a module. 
    """

    def __init__(
        self, 
        killchain_cat: StrEnum, 
        name: str, 
        function: Callable[[BinShellAbsClass, str], None], 
        help_text: str = "No help text provided."
    ):
        """
        :param killchain_cat: The category of the node's exploit in the kill chain.
        :param name: The name of the node's exploit.
        :param function: The exploit function to be executed.
        :param help_text: Help text for the node's exploit, defaults to "No help text provided."

        Initialize the node with details of its exploit.
        """

        self.killchain_cat = killchain_cat
        self.name = name
        self.function = function
        self.help_text = help_text

        self._edge_logic = None

    @property
    def edge_logic(self) -> EdgeLogic:
        """
        :return: The function that dictates which node to go 
            to next based on inputs of `status` and `data`. 

        Set the next node(s) to go to after executing this node.
        """

        return self._edge_logic

    @edge_logic.setter
    def edge_logic(self, edge_logic: EdgeLogic) -> None:
        """
        :param edge_logic: The function dictating which node to call next. 
            Accepts 2 arguments: `status` and `data`.
            Returns a Node.
        :return: None

        Set the next node(s) to go to after executing this node.
        """

        self._edge_logic = edge_logic

    def goto(self, status: int, data: dict[str, Any]) -> Optional[Self]:
        """
        :return: Next Node

        Returns the next node after executing this node.
        """

        if self._edge_logic is None:
            return
        
        return self._edge_logic(status, data)

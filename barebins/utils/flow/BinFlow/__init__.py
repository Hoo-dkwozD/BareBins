#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Subpackage with the abstract classes defining flow objects in exploit shells.

Flows follow a graph structure, where each node represents an exploit module &
dictates the execution flow to the next node.
"""

# Local application/library imports
from .BinNode import BinNodeAbsClass
from .BinGraph import BinGraphAbsClass

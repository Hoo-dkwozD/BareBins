#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Abstract class of the basic interactive shell for carrying out developed exploits.
Used to define the interface for the shell commands and their categories.
"""

# Python standard library imports
from abc import ABC, abstractmethod
from argparse import Namespace
from enum import Enum
from typing import Any, Dict

# Local application/library imports
from barebins.shellcore import BinCoreAbsClass

class BinShellAbsClass(ABC):
    """
    Abstract base class for a simple command line shell for carrying out developed exploits.
    """

    # Attributes
    name: str
    args: Namespace
    prompt: str
    mod_prompt: str
    intro: str
    core: BinCoreAbsClass

    # Methods
    @abstractmethod
    def __init__(self, name: str, args: Namespace):
        """
        Initialize a shell class for the exploit.
        """

        pass

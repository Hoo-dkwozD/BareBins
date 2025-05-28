#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Utility that simplifies the Colorama styling of the output in the terminal.
"""

# Third-party library imports
from colorama import Fore, Back, Style

class f:
    """
    Sets the foreground colors for terminal output.
    """

    B = Fore.BLACK
    r = Fore.RED
    g = Fore.GREEN
    y = Fore.YELLOW
    b = Fore.BLUE
    m = Fore.MAGENTA
    c = Fore.CYAN
    W = Fore.WHITE
    R = Fore.RESET

class b:
    """
    Sets the background colors for terminal output.
    """

    B = Back.BLACK
    r = Back.RED
    g = Back.GREEN
    y = Back.YELLOW
    b = Back.BLUE
    m = Back.MAGENTA
    c = Back.CYAN
    W = Back.WHITE
    R = Back.RESET

class s:
    """
    Sets the styles for terminal output.
    """

    D = Style.DIM
    N = Style.NORMAL
    B = Style.BRIGHT
    R = Style.RESET_ALL

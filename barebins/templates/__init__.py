#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Collection of templates for structural files needed to use this package.
"""

# Starter template for the exploit script
def start_template() -> str:
    """
    :returns: The multi-line string starter template for the exploit entry-point.

    This function reads the starter template from a file and returns it as a string.
    """

    START = ""

    ## Uses `starter.py`
    with open("starter.py", "r") as f:
        START = f.read()

    return START

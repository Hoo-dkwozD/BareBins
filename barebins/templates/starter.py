#!/usr/bin/env python3

"""
:author: 
:license: 
:version: 
:date: 
"""

# Python standard library imports
import os
import sys

# Third-party library imports
from colorama import init as colorama_init
from pyfiglet import figlet_format
from termcolor import cprint

# Local application/library imports
from barebins.shellcore import BinCore
from utils.argument import ArgHandler
from shell import BinShellManager
from utils.styles import f, s

# Initialize colorama
colorama_init(strip=not sys.stdout.isatty())

# Print the banner
cprint(
    figlet_format("barebins", font="big"),
    "blue",
    attrs=["bold"],
    end=f"\n"
)
cprint(
    figlet_format(os.path.basename(__name__), font="alphabet"),
    "blue",
    attrs=["bold"],
    end=f"\n\n"
)

def main():
    """
    :returns: None

    This function is the main entry point of the script. 
    It parses command-line arguments and starts an interactive shell session. 
    """

    # Initialize the argument handler
    arg_handler = ArgHandler(
        prog=os.path.basename(__file__),
        description="Exploit tool. ", # CHANGE ME
    )

    # Add command-line arguments
    arg_handler.add_verbose()
    options = []
    # -- CHANGE ME -- 
    options.append(
        ("-e", "--example", {"help": "An example option"})
    )
    # -- CHANGE ME --
    arg_handler.add_options(options)

    # Parse the command-line arguments
    args = arg_handler.parser.parse_args()

    shell = BinShellManager(os.path.basename(__file__), args)
    core = BinCore()
    shell.load_flow(core)
    shell.load_modules() # CHANGE ME
    shell.start()

if __name__ == "__main__":
    main()
else:
    print(f"{f.r}[!] This script is not meant to be imported.{s.R}")
    sys.exit(1)

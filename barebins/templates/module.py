#!/usr/bin/env python3

"""
:author: 
:license: 
:version: 
:date: 
"""

# Python standard library imports

# Third-party library imports
from barebins.module import BasicModule
from barebins.shell import BinShellAbsClass
from barebins.utils.argument import SubArgHandler
from barebins.utils.styles import f, s

# Local application/library imports

exploit_name = "example"  # -- CHANGE VALUE --

def exploit_function(self: BinShellAbsClass, args: str) -> None:
    """
    :param self: The instance of the shell class the module belongs to.
    :param args: The arguments for the module.

    A function that executes an exploit.
    """

    # Initialise the argument handler for this module
    arg_handler = SubArgHandler(
        name=exploit_name,
        description="Module for the shell.", # -- CHANGE ME --
    )

    # Add command-line arguments
    # -- CHANGE ME -- 
    arg_handler.add_verbose()
    options = []
    options.append(
        ("-e", "--example", {"help": "An example option"})
    )
    # -- CHANGE ME --
    arg_handler.add_options(options)

    # Parse the command-line arguments
    args = arg_handler.parse_args()

    print(f"{f.g}Entering {exploit_name} module... {s.R}")
    # -- CHANGE ME --
    # Add your module logic here
    print(args)
    data = {"example": "example data"}  # Example data for the module
    self.core.update(exploit_name, data)  # Update the core with the module data
    # -- CHANGE ME --

    # Exit scripts
    print(f"{f.g}Exiting {exploit_name} module... {s.R}")
    self.mod_prompt = self.prompt  # Reset the prompt to the shell's prompt
    print(f"{f.g}Exited {exploit_name} module.{s.R}")

# -- CHANGE MODULE NAME --
example_module = BasicModule(
    name=exploit_name,
    function=exploit_function
)

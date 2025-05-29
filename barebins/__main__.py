#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Main entry point for the Barebins exploit development tool.

It helps initialise exploit development files such as:
- An exploit script (init file to create a coordinating exploit shell)
- A core file (flow file to chain exploits)
- A module file (exploits, payloads, etc.)
"""

# Python standard library imports
import sys

# Third-party library imports
from colorama import init as colorama_init
from pyfiglet import figlet_format
from termcolor import cprint

# Local application/library imports
from barebins import templates
from barebins.utils.argument import ArgHandler
from barebins.utils.styles import f, s

def create_init(name: str, overwrite: bool = False) -> None:
    """
    :param name: The main name of the exploit script to be created.
    :param overwrite: If True, overwrite the file if it already exists.
    :returns: None

    This function initializes a file in the current directory that 
    forms the entry point of the exploit. 
    """

    if overwrite:
        with open(f"{name}.py", "w") as file:
            file.write(templates.start_template())
    else:
        with open(f"{name}.py", "x") as file:
            file.write(templates.start_template())

    print(f"{f.g}[+] `{name}.py` created successfully!{s.R}")
    print(f"{f.y}[!] Please edit the file and add your code.{s.R}")
    print(f"{f.y}[!] Then run it with the command: `python3 {name}.py{s.R}`")
    print(f"{f.g}[+] Good luck!{s.R}")

def create_module(name: str, overwrite: bool = False) -> None:
    """
    :param name: The name of the module to be created.
    :param overwrite: If True, overwrite the file if it already exists.
    :returns: None

    This function creates a new module file in the current directory 
    with the given name.
    """

    if overwrite:
        with open(f"{name}_module.py", "w") as file:
            file.write(templates.module_template())
    else:
        with open(f"{name}_module.py", "x") as file:
            file.write(templates.module_template())

    print(f"{f.g}[+] `{name}.py` created successfully!{s.R}")
    print(f"{f.y}[!] Please edit the file and add your code.{s.R}")
    print(f"{f.y}[!] Then modify the starter file to include the module.{s.R}")
    print(f"{f.g}[+] Good luck!{s.R}")

def create_flow(name: str, overwrite: bool = False) -> None:
    """
    :param name: The name of the core file to be created.
    :param overwrite: If True, overwrite the file if it already exists.
    :returns: None

    This function creates a new core file in the current directory.
    """

    if overwrite:
        with open(f"{name}_flow.py", "w") as file:
            file.write(templates.flow_template())
    else:
        with open(f"{name}_flow.py", "x") as file:
            file.write(templates.flow_template())

    print(f"{f.g}[+] `{name}_flow.py` created successfully!{s.R}")
    print(f"{f.y}[!] Please edit the file and add your code.{s.R}")
    print(f"{f.y}[!] Then modify the starter file to include the flow.{s.R}")
    print(f"{f.g}[+] Good luck!{s.R}")

def main() -> None:
    """
    :returns: None
    
    This function is the main entry point of the script. 
    It parses command-line arguments and calls the file creating functions.
    """

    # Initialize colorama
    colorama_init(strip=not sys.stdout.isatty())

    # Print the banner
    cprint(
        figlet_format("barebins", font="big"),
        "blue",
        attrs=["bold"],
        end="\n\n"
    )

    # Prepare the arguments
    handler = ArgHandler(
        name="barebins",
        description="Barebins - A simple exploit development tool.",
    )
    handler.add_options(
        [
            (
                "purpose", 
                {
                    "help": "The filetype to be created: init, core, module.",
                    "choices": ["init", "flow", "module"]
                }, 
            ),
            (
                "name", 
                {
                    "help": "The name of the file to be created."
                }, 
            ),
            (
                "-o", 
                "--overwrite", 
                {
                    "action": "store_true",
                    "help": "Overwrite the file if it already exists."
                }
            )
        ]
    )
    args = handler.parse_args()

    # Create the files based on the arguments
    if args.purpose == "init":
        if not args.name:
            print(f"{f.r}[!] Please provide a name for the init file.{s.R}")
            sys.exit(1)
        else:
            create_init(args.name, args.overwrite)
    elif args.purpose == "flow":
        if not args.name:
            print(f"{f.r}[!] Please provide a name for the flow file.{s.R}")
            sys.exit(1)
        else:
            create_flow(args.name, args.overwrite)
    elif args.purpose == "module":
        if not args.name:
            print(f"{f.r}[!] Please provide a name for the module file.{s.R}")
            sys.exit(1)
        else:
            create_module(args.name, args.overwrite)
    else:
        print(f"{f.r}[!] No proper arguments provided. Use -h for help.{s.R}")
        sys.exit(1)

# Ensure the script is being run as a module
if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Program to aid in the development of exploit code. 

It can be used to creat a set of python files that can be used to 
build an exploit from reconnaissance to action on objective. 
Alternatively, it can be used as a module directly to create exploits. 

It uses a structure similar to Metasploit with more flexibility added to it. 
It comes with only a simple set of pre-written modules, so that it can
be used in certification tests that do not allow the use of Metasploit.
"""

# Python standard library imports
import sys

# Third-party library imports
from colorama import init as colorama_init
from pyfiglet import figlet_format
from termcolor import cprint

# Local application/library imports
import templates
from utils.argument import ArgHandler
from utils.styles import f, s

def create_init(name: str) -> None:
    """
    :param name: The main name of the exploit script to be created.
    :returns: None

    This function initializes a file in the current directory that 
    forms the entry point of the exploit. 
    """

    with open(f"{name}.py", "x") as file:
        file.write(templates.start_template())

    print(f"{f.g}[+] `{name}.py` created successfully!{s.R}")
    print(f"{f.r}[!] Please edit the file and add your code.{s.R}")
    print(f"{f.r}[!] Then run it with the command: `python3 {name}.py{s.R}`")
    print(f"{f.g}[+] Good luck!{s.R}")

def create_module(name: str) -> None:
    """
    :param name: The name of the module to be created.
    :returns: None

    This function creates a new module file in the current directory 
    with the given name.
    """

    with open(f"{name}.py", "x") as file:
        file.write(templates.module_template())

    print(f"{f.g}[+] `{name}.py` created successfully!{s.R}")
    print(f"{f.r}[!] Please edit the file and add your code.{s.R}")
    print(f"{f.r}[!] Then modify the starter file to include the module.{s.R}")
    print(f"{f.g}[+] Good luck!{s.R}")

def create_core():
    """
    :param name: The name of the core file to be created.
    :returns: None

    This function creates a new core file in the current directory.
    """

    with open(f"core.py", "x") as file:
        file.write(templates.core_template())

    print(f"{f.g}[+] `core.py` created successfully!{s.R}")
    print(f"{f.r}[!] Please edit the file and add your code.{s.R}")
    print(f"{f.r}[!] Then modify the starter file to include the core.{s.R}")
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
        prog="barebins",
        description="Barebins - A simple exploit development tool.",
    )
    handler.add_options(
        [
            (
                "purpose", 
                {
                    "help": "The filetype to be created: init, core, module.",
                    "choices": ["init", "core", "module"]
                }, 
            ),
            (
                "name", 
                {
                    "help": "The name of the file to be created.",
                    "nargs": "?"
                }, 
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
            create_init(args.name)
    elif args.purpose == "core":
        create_core()
    elif args.purpose == "module" and args.name:
        if not args.name:
            print(f"{f.r}[!] Please provide a name for the init file.{s.R}")
            sys.exit(1)
        else:
            create_module(args.name)
    else:
        print(f"{f.r}[!] No proper arguments provided. Use -h for help.{s.R}")
        sys.exit(1)

# Ensure the script is being run as a module
if __name__ == "__main__":
    main()

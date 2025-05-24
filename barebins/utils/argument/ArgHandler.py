#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Simplifies the handling of command-line arguments for the exploit.
"""

# Python standard library imports
import argparse
from typing import Any, Dict, Optional, Union

class ArgHandler():
    """
    A class to handle command-line arguments for the exploit.
    """

    def __init__(self, name: str, description: str, **kwargs: Dict[str, Any]) -> None:
        """
        :param name: The name of the program.
        :param description: A brief description of the program.
        :param kwargs: Additional arguments for the argument parser.
        :return: ArgHandler object.

        Initializes the argument parser with the given name and description.
        """

        self.parser = argparse.ArgumentParser(
            prog=name,
            description=description,
            **kwargs
        )

    def add_verbose(self, description: str = 'Enables verbose output') -> None:
        """
        :param description: A brief description of the verbose option.
        :return: None

        Adds a verbose argument to the parser.
        """

        self.parser.add_argument('-v', '--verbose', action='store_true', help=description)

    def add_option(self, names: Union[str, (str, str)], config: Dict[str, Any]):
        """
        :param names: The name(s) of the option. 
            Can be a single string (positional arg) or a tuple of strings (flags).
        :param config: A dictionary containing option details.
        :return: None

        Adds options to the parser based on the provided configuration dictionary.
        """

        if type(names) is str:
            self.parser.add_argument(names, **config)
        else:
            self.parser.add_argument(*names, **config)

    def add_options(self, options: list[(str, Optional[str], dict[str, Any])]):
        """
        :param options: A list of tuples containing option names and details.
        :return: None
        :raises ValueError: If the option format is invalid.

        Adds multiple options to the parser.
        """

        for option in options:
            if len(option) == 2:
                self.add_option(option[0], {'help': option[1]})
            elif len(option) == 3:
                self.add_option(option[0], option[2])
            else:
                raise ValueError("Invalid option format. Expected (name, description, config).")

    def parse_args(self, args: Optional[list[str]] = None) -> argparse.Namespace:
        """
        :param args: A list of command-line arguments to parse. If None, uses sys.argv.
        :return: The parsed arguments as a Namespace object.

        Parses the command-line arguments.
        """

        return self.parser.parse_args(args)

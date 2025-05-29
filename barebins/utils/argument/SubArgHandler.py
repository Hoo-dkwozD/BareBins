#!/usr/bin/env python3

"""
:author: Hoo-dkwozD
:license: GPLv3
:version: 0.1
:date: 2025-05-23

Simplifies the handling of command-line arguments for 
the commands within the exploit shell.
"""

# Python standard library imports
import argparse
from collections import defaultdict
import os
from string import Template
from typing import Any, Union

# Local application/library imports
from barebins.utils.argument.ArgHandler import ArgHandler

# Local types
type ArgumentConfig = dict[str, Any]
type Argument = Union[tuple[str, ArgumentConfig], tuple[str, str, ArgumentConfig]]

class SubArgHandler:
    """
    A class to handle command-line arguments within the exploit shell.
    """

    def __init__(self, name: str, description: str, **kwargs: dict[str, Any]):
        """
        :param name: The name of the command.
        :param description: A brief description of the command.
        :return: SubArgHandler object.

        Initializes the command handler with the given name and description.
        """

        if "add_help" not in kwargs:
            kwargs["add_help"] = False

        self.arg_handler = ArgHandler(
            name=name,
            description=description,
            **kwargs
        )

    def _expandvars(self, args: str) -> str:
        """
        :param args: A string of command-line arguments to have env variables expanded.
        :return: The expanded form of the arguments.

        Expands environment variables in the provided arguments.
        """

        env = defaultdict(lambda: "") # Default to empty string for missing vars
        env.update(os.environ) # Load current environment variables
        return Template(args).substitute(env)

    def add_verbose(self, description: str = 'Enables verbose output') -> None:
        """
        :param description: A brief description of the verbose option.
        :return: None

        Adds a verbose argument to the parser.
        """

        self.arg_handler.add_verbose(description)

    def add_option(self, names: Union[str, tuple[str, str]], config: ArgumentConfig) -> None:
        """
        :param names: The name(s) of the option. 
            Can be a single string (positional arg) or a tuple of strings (flags).
        :param config: A dictionary containing option details.
        :return: None

        Adds options to the parser based on the provided configuration dictionary.
        """

        self.arg_handler.add_option(names, config)

    def add_options(self, options: list[Argument]) -> None:
        """
        :param options: A list of tuples containing option names and details.
        :return: None
        :raises ValueError: If the option format is invalid.

        Adds multiple options to the parser.
        """

        self.arg_handler.add_options(options)

    def parse_args(self, args: str) -> argparse.Namespace:
        """
        :param args: A string of command-line arguments to parse.
        :return: The parsed arguments as a Namespace object.

        Parses the command-line arguments.
        """

        exp_args = self._expandvars(args)
        args_seq = exp_args.split()

        return self.arg_handler.parse_args(args_seq)

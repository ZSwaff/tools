#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Common Python functions and classes."""


import builtins
import sys
import traceback
from functools import wraps


RPCL_CD_DELIM = '`'


def rpcl_safe(fn):
    """Annotation for RPCL methods to ensure safe finish."""
    @wraps(fn)
    def wrapper():
        try:
            fn()
        except Exception as ex:
            if isinstance(ex, SystemExit):
                raise
            print(traceback.format_exc())
            print(f'{RPCL_CD_DELIM}.')

    return wrapper


class RpclManager:
    """A class to manage the Run Print Cd Ls client relationship."""

    def __init__(self, parser):
        """Prepares the parser.

        Args:
            parser (argparser.ArgumentParser): The parser to build on.
        """
        self.__parser = parser
        self.__parser.add_argument('--rpcl-input-args', required=True)
        self.__old_parse_args = self.__parser.parse_args
        self.__parser.parse_args = self.parse_args

        self.__input_args = None
        self.__input_index = 0

        self.__old_print = builtins.print
        builtins.print = self.print
        self.__old_input = builtins.input
        builtins.input = self.input
        builtins.exit = self.exit

    def __raise_if_unparsed(self):
        if self.__input_args is None:
            raise RuntimeError('parse_args has not been called')

    def parse_args(self):
        """Parses the args from the command line.

        Returns:
            (argparser.Namespace): The argparser-parsed args.
        """
        args = self.__old_parse_args()
        input_args_str = args.rpcl_input_args[1:-1]
        if len(input_args_str) != 0:
            self.__input_args = input_args_str[1:-1].split('""')
        else:
            self.__input_args = []
        delattr(args, 'rpcl_input_args')
        return args

    def input(self):
        """Gets the appropriate input from the user, one way or another.

        Returns:
            (str): The user input.
        """
        self.__raise_if_unparsed()
        if self.__input_index == len(self.__input_args):
            self.exit()
        self.__input_index += 1
        return self.__input_args[self.__input_index - 1]

    def print(self, *args, **kwargs):
        """Print a message appropriately (only the first time)."""
        self.__raise_if_unparsed()
        if self.__input_index == len(self.__input_args):
            self.__old_print(*args, **kwargs)

    def exit(self, *args, **kwargs):
        """Print the return message and exits."""
        self.__raise_if_unparsed()
        self.__old_print(f'{RPCL_CD_DELIM}', end='')
        if len(args) == 0:
            args = ('.',)
        self.__old_print(*args, **kwargs)
        self.close()
        sys.exit(0)

    def close(self):
        """Cleans up the manager."""
        self.__raise_if_unparsed()
        builtins.print = self.__old_print
        builtins.input = self.__old_input
        delattr(builtins, 'exit')

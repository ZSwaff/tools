#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Common Python functions and classes."""


import builtins
import sys
import subprocess


def ignore_null(func):
    """Ignores null arguments on the input function."""
    def wrapper(*args):
        if func is None or all(e is None for e in args):
            return None
        return func(e for e in args if e is not None)
    return wrapper


def load_f(fname):
    """Loads a file."""
    with open(os.path.expanduser(fname)) as fin:
        return fin.read()


def load_j(fname):
    """Loads a file as JSON."""
    with open(os.path.expanduser(fname)) as fin:
        return json.load(fin)


def run_command(cmd, path=None, verbose=False):
    """Runs a command in a directory and (maybe) prints the command at the
    output.

    Args:
        cmd (str): The command to run.
        path (str): The path to run it under.
        verbose (bool): Whether to print the command and its results.

    Returns:
        (str): The result of the command.
    """
    if verbose:
        print(cmd)
    result = subprocess.check_output(cmd, cwd=path, shell=True).decode()
    if verbose:
        print(' > ' + result)
    return result


class RpclIOManager:
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
        self.__old_print('`', end='')
        self.__old_print(*args, **kwargs)
        self.close()
        sys.exit(0)

    def close(self):
        """Cleans up the manager."""
        self.__raise_if_unparsed()
        builtins.print = self.__old_print
        builtins.input = self.__old_input
        delattr(builtins, 'exit')

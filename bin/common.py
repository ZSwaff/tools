#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Common Python functions and classes."""


import os
import subprocess
from datetime import datetime

from termcolor import colored


RPCL_CD_DELIM = '`'


def is_ipynb():
    """Returns whether the current environment is an iPython Notebook.

    Returns:
        (bool): Whether the current environment is an iPython Notebook.
    """
    try:
        get_ipython()
        return True
    except NameError:
        return False


def now():
    """Returns the datetime now in UTC.

    Returns:
        (datetime.datetime): The datetime now.
    """
    return datetime.utcnow()


def iso(dt=None):
    """Returns a datetime as a string.

    Args:
        dt (datetime): The datetime to format.

    Returns:
        (str): The datetime as a string.
    """
    if dt is None:
        dt = now()
    return dt.isoformat() + 'Z'


def from_iso(dt_str):
    """Returns a datetime from a string.

    Args:
        dt_str (str): The datetime to parse.

    Returns:
        (datetime): The datetime.
    """
    return datetime.strptime(dt_str, '%Y-%m-%dT%H:%M:%S.%fZ')


def epoch(dt=None):
    """Returns a datetime as seconds from the epoch.

    Args:
        dt (datetime): The datetime to format.

    Returns:
        (float): The datetime as seconds from the epoch.
    """
    if dt is None:
        dt = now()
    return dt.timestamp()


def ignore_null(func):
    """Ignores null arguments on the input function.

    Args:
        func (function): The function to wrap.

    Returns:
        (function): The wrapped function.
    """
    def wrapper(*args):
        if func is None or all(e is None for e in args):
            return None
        return func(e for e in args if e is not None)
    return wrapper


def load_f(fname):
    """Loads a file.

    Args:
        fname (str): The file path to load.

    Returns:
        (str): The contents of the loaded file.
    """
    with open(os.path.expanduser(fname)) as fin:
        return fin.read()


def load_j(fname):
    """Loads a file as JSON.

    Args:
        fname (str): The file path to load.

    Returns:
        (dict): The contents of the loaded JSON file.
    """
    with open(os.path.expanduser(fname)) as fin:
        return json.load(fin)


def color_info(s):
    """Color an object as info.

    Args:
        s (str): The object to color.

    Returns:
        (dict): The colored object.
    """
    return colored(str(s), 'blue')


def color_err(s):
    """Color an object as error.

    Args:
        s (str): The object to color.

    Returns:
        (dict): The colored object.
    """
    return colored(str(s), 'red')


def color_succ(s):
    """Color an object as success.

    Args:
        s (str): The object to color.

    Returns:
        (dict): The colored object.
    """
    return colored(str(s), 'green')


def run_command(cmd, path=None, verbose=False):
    """Runs a command in a directory and (maybe) prints the command and the
    output.

    Args:
        cmd (str): The command to run.
        path (str): The path to run it under.
        verbose (bool): Whether to print the command and its results.

    Returns:
        (str): The result of the command.
    """
    if verbose:
        print(color_info(cmd))
    try:
        result = subprocess.check_output(cmd, cwd=path, shell=True).decode()
    except subprocess.CalledProcessError as ex:
        if verbose:
            print(color_err(ex))
        raise
    if verbose:
        print(color_succ(result))
    return result

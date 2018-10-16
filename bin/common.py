#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Common Python functions."""

import subprocess

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

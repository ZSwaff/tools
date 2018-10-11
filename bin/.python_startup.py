#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Common Python functions."""


# Basic Imports
import sys
import os
import math
import time
import datetime
import random
import json
import re
import subprocess
import types

import numpy as np
import pandas as pd

import plentyservice
import plenty_data_frames

from common import *


# Functions
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


# JSON
false = False
true = True
null = None


# Default Values
s = 'abc'
l = [1, 2, 3]
d = {1: 2, 2: 3, 3: 4}
t = (1, 2, 3)


# iPython and Builtins
q = exit
min = ignore_null(min)
max = ignore_null(max)


# Plenty
__plenty_client_builder = plentyservice.client_builder()
c = types.SimpleNamespace(**{
    e[6]: getattr(__plenty_client_builder, e)()
    for e in dir(__plenty_client_builder)
    if e.startswith('build')
})

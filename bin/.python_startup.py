#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Common Python functions."""


import sys
import os
import math
import time
import datetime
import random
import json
import re
import subprocess

import numpy as np
import pandas as pd

import plentyservice
import plenty_data_frames

from common import *


def ignore_null(func):
    """Ignores null arguments on the input function"""
    def wrapper(*args):
        if func is None or all(e is None for e in args):
            return None
        return func(e for e in args if e is not None)
    return wrapper


false = False
true = True
null = None

s = 'abc'
l = [1, 2, 3]
d = {1: 2, 2: 3, 3: 4}
t = (1, 2, 3)

q = exit

min = ignore_null(min)
max = ignore_null(max)

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
import argparse

import numpy as np
import pandas as pd

import plentyservice
if sys.version_info > (3, 0):
    import plenty_data_frames

from common import *


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
__plenty_clients = {
    e[6]: getattr(__plenty_client_builder, e)()
    for e in dir(__plenty_client_builder)
    if e.startswith('build')
}
if sys.version_info > (3, 3):
    c = types.SimpleNamespace(**__plenty_clients)
else:
    c = lambda: None
    for k, v in __plenty_clients.items():
        setattr(c, k, v)

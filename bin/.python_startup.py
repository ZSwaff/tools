#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Common Python functions."""


# Basic Imports
import sys
import os
import math
import time
from datetime import datetime, timedelta
import random
import json
import csv
import re
import subprocess
import argparse
import inspect

import requests
import numpy as np
import pandas as pd

import plentyservice

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
cli = lambda: None
for attr in dir(__plenty_client_builder):
    if not attr.startswith('build'):
        continue
    setattr(cli, attr[6:-7], getattr(__plenty_client_builder, attr)())

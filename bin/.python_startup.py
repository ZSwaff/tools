import sys
import os
import time
import datetime
import random

import numpy as np

import plentyservice


false = False
true = True
null = None

l = [1, 2, 3, 4, 5]
d = {1: 2, 2: 3, 3: 4}
t = (1, 2, 3)

q = exit

def rand_sn(n=1, prefix='', suffix='', sn_format='{}{}{}{}-{}{}{}{}-{}{}{}'):
	def to_let(i):
		if i < 10: 
			return str(i)
		return chr(i - 10 + ord('A'))
	res = []
	for i in range(n):
		lst = [to_let(random.randint(0, 35)) for j in range(10)]
		res.append(prefix + sn_format.format(*lst) + suffix)
	return res

def rand_towers(n=1):
	return rand_sn(n, '', '', 'Tower:0_0_1:{0}{1}{2}{3}-{4}{5}{6}{7}-{8}{9}, {0}{1}{2}{3}, Tower:0_0_1:{0}{1}{2}{3}-{4}{5}{6}{7}-{8}{9}')

def rand_trays(n=1):
	return rand_sn(n, '', '', 'Tray:0_0_1:{0}{1}{2}{3}-{4}{5}{6}{7}-{8}{9}, {0}{1}{2}{3}, Tray:0_0_1:{0}{1}{2}{3}-{4}{5}{6}{7}-{8}{9}')

def tower_loc(room, row, tower, site='SSF1'):
	return 'T:{}-{}-{}-{}'.format(site, room, row, tower)

def formatted_tower_locs(room, rows, towers, site='SSF1'):
	locs = [(chr(r), str(n)) for r in range(ord('A'), ord('A') + rows) for n in range(1, towers + 1)]
	t_locs = [tower_loc(room, row, tower, site) for row, tower in locs]
	return ['{0}, {1}, {0}'.format(e, '-'.join(e.split('-')[-2:])) for e in t_locs]

def tray_loc(room, cart, level, spot, site='SSF1'):
	return 'Y:{}-{}-{}-{}-{}'.format(site, room, cart, level, spot)

def formatted_tray_locs(room, carts, levels, spots, site='SSF1'):
	locs = [(str(c), chr(l), str(s)) for c in carts for l in range(ord('A'), ord('A') + levels) for s in range(1, spots + 1)]
	t_locs = [tray_loc(room, cart, level, spot, site) for cart, level, spot in locs]
	return ['{0}, {1}, {0}'.format(e, '-'.join(e.split('-')[-3:])) for e in t_locs]

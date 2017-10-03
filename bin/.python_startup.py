import sys
import time
import os
import random

import numpy as np

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

# Trays
# print '\n'.join(rand_sn(30, '', '', 'Tray:0_0_1:{0}{1}{2}{3}-{4}{5}{6}{7}-{8}{9}, {0}{1}{2}{3}, Tray:0_0_1:{0}{1}{2}{3}-{4}{5}{6}{7}-{8}{9}'))
# Towers
# print '\n'.join(rand_sn(12, '', '', 'Tower:0_0_1:{0}{1}{2}{3}-{4}{5}{6}{7}-{8}{9}, {0}{1}{2}{3}, Tower:0_0_1:{0}{1}{2}{3}-{4}{5}{6}{7}-{8}{9}'))

import sys
import time
import os
import random

import numpy as np

l = [1, 2, 3, 4, 5]
d = {1: 2, 2: 3, 3: 4}
t = (1, 2, 3)

q = exit

def rand_sn(prefix='', n=1):
	def to_let(i):
		if i < 10: 
			return str(i)
		return chr(i - 10 + ord('A'))
	res = []
	for i in range(n):
		lst = [to_let(random.randint(0, 35)) for j in range(10)]
		res.append('{}{}{}{}{}-{}{}{}{}-{}{}'.format(prefix, *lst))
	return res

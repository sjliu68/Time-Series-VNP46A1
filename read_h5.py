# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 23:44:38 2019

@author: SJ
"""

import h5py
filename = 'VNP46A1.A2019091.h29v06.001.2019092100056.h5'
f = h5py.File(filename, 'r')

# List all groups
print("Keys: %s" % f.keys())
a = list(f.keys())[0]
b = list(f[a].keys())[1]
c = list(f[a][b].keys())[0]
d = list(f[a][b][c].keys())[0]
e = list(f[a][b][c][d].keys())
data = f[a][b][c][d]
data = data[e[4]]
# Get the data
data = list(f[a_group_key])
a = f[data[0]]

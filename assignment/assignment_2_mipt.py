#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 11:52:17 2022

@author: jimmy
"""

import math
import numpy as np
import matplotlib.pyplot as plt
 
from itertools import cycle
from functools import partial
from mpmath import mp
 
      
def f(x, ctx=math):
    return ctx.sin(x / 5) * ctx.exp(x / 10) + 5 * ctx.exp(-x / 2)
 
 
def approx_f(x, ws):
    return sum(x**i * w for i, w in enumerate(ws))
 
 
def a_matrix(xs, *, matrix=lambda x: x):
    return matrix([[x**n for n in range(len(xs))] for x in xs])
 
    
def b_matrix(xs, f, *, matrix=lambda x: x):
    return matrix([f(x) for x in xs])
 
 
def plot(fs, xlim, points=200):
    a, b = xlim
    colors = cycle(['b', 'r', 'g', 'm', 'k'])
    fig, ax = plt.subplots()
    xs = np.arange(a, b, (b-a)/points)
    for f, clr in zip(fs, colors):
        ys = [f(x) for x in xs]
        ax.plot(xs, ys, linewidth=2)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.grid(True)
    plt.show()
   
 
xpoints = [
    (1, 15),
    (1, 8, 15),
    (1, 4, 10, 15),
]
 
fs = [f]
for xs in xpoints:
    a = a_matrix(xs)
    b = b_matrix(xs, f)
    # ws = mp.lu_solve(a, b)
    # ws = scipy.linalg.solve(a, b)
    ws = np.linalg.solve(a,b)
    tf = partial(approx_f, ws=ws)
    fs.append(tf)
 
# mp.plot(fs, (0, 16))
plot(fs, (0, 16))
print('Result', ws)


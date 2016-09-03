import numpy as np
from scipy.optimize import linprog

d = [166.67, 74.08, 222.23, 268.52, 250, 120.38]
d = np.array(d)
# d *= 1.08
# Doesn't have solution if demand increases 8% !!!

c1 = np.array([1, 1, 1, 1, 1, 1])
c2 = np.array([1, 1, 1, 1, 1])
c = np.concatenate((c1 * 1000, c2 * 100))

A_eq = [
    [1, 0, 0, 0, 0, 0,
     -1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0,
     1, -1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0,
     0, 1, -1, 0, 0],
    [0, 0, 0, 1, 0, 0,
     0, 0, 1, -1, 0],
    [0, 0, 0, 0, 1, 0,
     0, 0, 0, 1, -1],
    [0, 0, 0, 0, 0, 1,
     0, 0, 0, 0, 1]]
b_eq = [-60., 0, 0, 0, 0, 50.]
b_eq = np.array(b_eq)
b_eq += d

bounds = (
    (0, 150), (0, 195), (0, 210), (0, 255), (0, 190), (0, 220),
    (0, None), (0, None), (0, None), (0, None), (0, None))

res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
print(res)

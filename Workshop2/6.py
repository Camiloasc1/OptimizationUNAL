import numpy as np
from scipy.optimize import linprog

c = [10, 3.8, 1.5]

A_ub = [
    [1, 1, 1],
    [-1, -1, -1],
    [-1, -1. / 3., -1. / 6.]]
b_ub = [18, -12, -9]

res = linprog(c, A_ub=A_ub, b_ub=b_ub)
print(res)

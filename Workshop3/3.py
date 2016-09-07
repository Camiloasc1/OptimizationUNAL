import numpy as np
from scipy.optimize import linprog

c = np.array([6, 8]) * 100000
A_ub = [
    [1, 1],
    [-40, -50]
]
b_ub = [9, -400]

bounds = ((0, 8), (0, 10))

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(res)

import numpy as np
from scipy.optimize import linprog

c1 = np.array([0.3, 0.2]) * -1
c2 = np.array([4.5, 1.5])
A_ub = [
    [-1, 1],
    [1, 1],
    [-1, -1]
]
b_ub = [0, 150, -50]

bounds = ((0, 100), (0, None))

res = linprog(c1, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(res)
res = linprog(c2, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(res)

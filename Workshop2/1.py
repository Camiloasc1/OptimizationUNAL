import numpy as np
from scipy.optimize import linprog

c = np.array([5, 4, 10]) * -1
A_ub = [[1. / 30., 1. / 50., 1. / 20.], [1, -1, 1]]
b_ub = [1, 0]

res = linprog(c, A_ub=A_ub, b_ub=b_ub)
print(res)

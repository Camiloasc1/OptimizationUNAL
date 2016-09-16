import numpy as np
from scipy.optimize import linprog

c = np.array([6, 8]) * 100000
A_ub = [
    [1, 1],
    [-40, -50]
]
b_ub = [9, -400]

bounds = ((0, 8), (0, 10))


def callback(xk, **kwargs):
    np.set_printoptions(precision=3)
    np.set_printoptions(suppress=True)
    print(kwargs)


res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, callback=callback)
print(res)

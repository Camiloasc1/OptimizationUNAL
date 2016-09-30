import numpy as np
from scipy.optimize import linprog

c = np.array([32, 72, 4, 12])
A_ub = [
    [-1, 0, -1, 0],
    [0, -3, -1, 0],
    [-2, 0, 0, -1],
    [0, -4, 0, -1]
]
b_ub = [-40, -40, -60, -60]

bounds = ((0, None), (0, None), (None, 0), (None, 0))


def callback(xk, **kwargs):
    np.set_printoptions(precision=3)
    np.set_printoptions(suppress=True)
    print(kwargs)


res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, callback=callback)
print(res)

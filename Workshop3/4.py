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


def callback(xk, **kwargs):
    np.set_printoptions(precision=3)
    np.set_printoptions(suppress=True)
    print(kwargs)


res = linprog(c1, A_ub=A_ub, b_ub=b_ub, bounds=bounds, callback=callback)
print(res)
res = linprog(c2, A_ub=A_ub, b_ub=b_ub, bounds=bounds, callback=callback)
print(res)

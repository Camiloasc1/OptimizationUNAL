import numpy as np
from scipy.optimize import linprog

c = np.array([2, 1.5]) * -1 * 1000
A_ub = [
    [1, 1],
    [0.25, 0.2]
]
b_ub = [900, 200]


def callback(xk, **kwargs):
    np.set_printoptions(precision=3)
    np.set_printoptions(suppress=True)
    print(kwargs)


res = linprog(c, A_ub=A_ub, b_ub=b_ub, callback=callback)
print(res)

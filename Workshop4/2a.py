import numpy as np
from scipy.optimize import linprog

c = np.array([40, 40,
              60, 60]) * -1
A_ub = [
    [1, 0,
     2, 0],
    [0, 3,
     0, 4],
    [-1, -1,
     0, 0],
    [0, 0,
     -1, -1]
]
b_ub = [32, 72, -4, -12]


def callback(xk, **kwargs):
    np.set_printoptions(precision=3)
    np.set_printoptions(suppress=True)
    print(kwargs)


res = linprog(c, A_ub=A_ub, b_ub=b_ub, callback=callback)
print(res)

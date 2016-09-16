import numpy as np
from scipy.optimize import linprog

c = np.array([0, 0, 1.7,
              0, 3]) * -1
A_eq = [
    [1, 0, 0,
     1, 0],
    [1.7, -1, 0,
     0, -1],
    [0, 1.7, -1,
     3, 0]
]
b_eq = [100000, 0, 0]


def callback(xk, **kwargs):
    np.set_printoptions(precision=3)
    np.set_printoptions(suppress=True)
    print(kwargs)


res = linprog(c, A_eq=A_eq, b_eq=b_eq, callback=callback)
print(res)
print(100000 * 1.7 * 3.0)

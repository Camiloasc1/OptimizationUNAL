import numpy as np
from scipy.optimize import linprog

c = np.array([0, 0, 1.7,
              0, 3,
              0, 0, 1]) * -1
A_eq = [
    [1, 0, 0,
     1, 0,
     1, 0, 0],
    [1.7, -1, 0,
     0, -1,
     1, -1, 0],
    [0, 1.7, -1,
     3, 0,
     0, 1, -1]
]
b_eq = [100000, 0, 0]

res = linprog(c, A_eq=A_eq, b_eq=b_eq)
print(res)
print(100000 * 1.7 * 3.0)

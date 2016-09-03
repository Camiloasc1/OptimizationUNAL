import numpy as np
from scipy.optimize import linprog

c = np.array([
    [2, 3, 5],
    [2.5, 4, 4.9],
    [3, 3.6, 3.2]
]).reshape(-1)

A_eq = [
    [1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1]]
b_eq = [500, 700, 600]

A_ub = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1]]
b_ub = [500]

bounds = (
    (0, None), (0, None), (0, None),
    (0, 200), (0, 200), (0, 200),
    (0, 200), (0, 200), (0, 200))

res = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(res)

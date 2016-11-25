import numpy as np
from scipy.optimize import linprog

c = np.array([2, -1, 1, 0, 0, 0]) * -1
A_eq = [
    [2, 1, -2, 1, 0, 0],
    [4, -1, 2, 0, -1, 0],
    [2, 3, -1, 0, 0, -1]
]
b_eq = [8, 2, 4]


def callback(xk, **kwargs):
    np.set_printoptions(precision=3)
    np.set_printoptions(suppress=True)
    print(kwargs)
    np.savetxt(__file__[:-3] + 'Tableau' + str(kwargs['phase']) + '-' + str(kwargs['nit']) + '.csv', kwargs['tableau'],
               delimiter=',', fmt='%.3f')


res = linprog(c, A_eq=A_eq, b_eq=b_eq, callback=callback)
print(res)

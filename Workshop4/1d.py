import numpy as np
from scipy.optimize import linprog

c = np.array([10, 1, 3]) * -1
A_ub = [
    [1, 1, 1],
    [1, -1, -1],
    [1, 2, 0]
]
b_ub = [5, 2, 1]


def callback(xk, **kwargs):
    np.set_printoptions(precision=3)
    np.set_printoptions(suppress=True)
    print(kwargs)
    np.savetxt(__file__[:-3] + 'Tableau' + str(kwargs['phase']) + '-' + str(kwargs['nit']) + '.csv', kwargs['tableau'],
               delimiter=',', fmt='%.3f')


res = linprog(c, A_ub=A_ub, b_ub=b_ub, callback=callback)
print(res)

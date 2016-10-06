import numpy as np
from scipy.optimize import linprog

c = np.array([3, 6, 2]) * -1
A_ub = [
    [3, -4, 1],
    [1, 2, 3]
]
b_ub = [2, 1]


def callback(xk, **kwargs):
    np.set_printoptions(precision=3)
    np.set_printoptions(suppress=True)
    print(kwargs)
    np.savetxt(__file__[:-3] + 'Tableau' + str(kwargs['phase']) + '-' + str(kwargs['nit']) + '.csv', kwargs['tableau'],
               delimiter=',', fmt='%.3f')


res = linprog(c, A_ub=A_ub, b_ub=b_ub, callback=callback)
print(res)

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
b_ub = [42, 72, -4, -12]


def callback(xk, **kwargs):
    np.set_printoptions(precision=3)
    np.set_printoptions(suppress=True)
    print(kwargs)
    np.savetxt('Tableau' + str(kwargs['phase']) + '-' + str(kwargs['nit']) + '.csv', kwargs['tableau'], delimiter=',',
               fmt='%.3f')


res = linprog(c, A_ub=A_ub, b_ub=b_ub, callback=callback)
print(res)

Binv1 = [
    [1, 0, -1, -2],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
Binv2 = [
    [0, 0.25, 0, -1],
    [0, 0.25, 0, 0],
    [1, 0, 1, 2],
    [1, 0, 0, 2]
]
b_n = [42, 72, 4, 12]

b_n = np.dot(Binv1, b_n)
b_n = np.dot(Binv2, b_n)
print(b_n)

from scipy.optimize import linprog

c = [5, 1]
A_ub = [[-2, -1], [-1, -1], [-2, -10]]
b_ub = [-6, -4, -20]
bounds = ((0, None), (0, None))

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(res)

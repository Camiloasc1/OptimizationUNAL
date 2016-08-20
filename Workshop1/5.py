from scipy.optimize import linprog

c = [100, 90, 120, 80]
A_ub = [[1, 1, 0, 0], [0, 0, 1, 1], [-500, 0, -650, 0], [0, -400, 0, -350]]
b_ub = [100, 100, -11000, -7000]
bounds = ((0, None), (0, None), (0, None), (0, None))

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(res)

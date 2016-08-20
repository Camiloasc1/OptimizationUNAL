from scipy.optimize import linprog

c = [-120, -90]
A_ub = [[0.3, 0.4], [0.5, 0.2], [0.2, 0.4]]
b_ub = [100, 120, 100]
bounds = ((0, None), (0, None))

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(res)

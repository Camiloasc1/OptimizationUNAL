from scipy.optimize import linprog

c = [-5, 1]
A_ub = [[-2, -3], [-1, 3]]
b_ub = [-12, 0]
bounds = ((0, None), (0, None))

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(res)

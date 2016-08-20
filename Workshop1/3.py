from scipy.optimize import linprog

c = [4, 1]
A_ub = [[-3, -1], [-4, -1], [-1, 0]]
b_ub = [-6, -12, -2]
bounds = ((0, None), (0, None))

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(res)

import numpy as np
import statsmodels.api as sm

# room temperature
Y = [18, 17, 18, 19, 20, 20, 21, 22, 22, 24, 25, 26, 28, 29, 28, 27, 25, 24, 24, 23, 22, 20, 19, 19]
X = range(1, 25)
X = sm.add_constant(X)

model = sm.OLS(Y, X)
results = model.fit()

# print
print(results.params)
print(results.tvalues)


print(results.t_test([1, 0]))
print(results.f_test(np.identity(2)))



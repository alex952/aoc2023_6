# Mathematical approach we can represent the inequality such as
# (t - x) * x > d
# tx - x**2 > d
# -x**2 + tx - d > 0

# Classic quadratic formula
# Coefficients would be:
# a = -1
# b = t
# c = -d
# Solve for x given that x needs to be integer the solutions
# solving for > 0 would be ceil of + side and floor of - side

t = 7
d = 9

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, t, 1)

a = -1
b = t
c = -d

y = a * (x**2) + b * x + c
plt.plot(x, y)
plt.show()

import numpy as np
from lab_3_task1 import acceleration_of_gravity as g

v0 = int(input('v0 = '))
x0 = int(input('x0 = '))
y0 = int(input('y0 = '))

N = 10

coords = np.zeros((N, 3))
t = np.linspace(0, 5, N)
x = x0 + v0 * t 
y = y0 + v0 * t - g * t ** 2 / 2

for i in range(N):
 coords[i, 0] = t[i]
 coords[i, 1] = x[i]
 coords[i, 2] = y[i]
print(coords)

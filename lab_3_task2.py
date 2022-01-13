import lab_3_task1 as m
import numpy as np
g = m.gravity_constant
p = m.pi
h = 100
a = p / 3
b = 0.523

v = np.sqrt(g * h * np.tan(b)**2/(2 * np.cos(a)**2 * ( 1 - np.tan(b) * np.tan(a))))
print(v)

from lab_3_task1 import eil as e

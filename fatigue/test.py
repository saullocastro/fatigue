import numpy as np
import pyximport; pyximport.install()
from rainflow import rainflow

a = np.array([0, -1, 1., 0, -1, 1, 0., -1, 1, 0., -1, 1, 0]) * 10
a[6:] /= 2
out = rainflow(a)
print(out)

